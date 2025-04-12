import mlflow
import optuna
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split, KFold
from optuna.integration.mlflow import MLflowCallback
from sklearn.metrics import accuracy_score
import numpy as np


iris = load_iris()
X, y = iris.data, iris.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

cv = KFold(n_splits=5, shuffle=True, random_state=42)

def objective(trial):
    n_estimators = trial.suggest_int('n_estimators', 50, 300, step=50)
    max_depth = trial.suggest_categorical('max_depth', [None, 5, 10, 15, 20])
    min_samples_split = trial.suggest_categorical('min_samples_split', [2, 5, 10])
    min_samples_leaf = trial.suggest_categorical('min_samples_leaf', [1, 2, 4])
    bootstrap = trial.suggest_categorical('bootstrap', [True, False])

    model = RandomForestClassifier(
        n_estimators=n_estimators,
        max_depth=max_depth,
        min_samples_split=min_samples_split,
        min_samples_leaf=min_samples_leaf,
        bootstrap=bootstrap,
        random_state=42
    )

    accuracy = []
    for step, (train_idx, val_idx) in enumerate(cv.split(X_train, y_train)):
        X_train_fold, X_val_fold = X_train[train_idx], X_train[val_idx]
        y_train_fold, y_val_fold = y_train[train_idx], y_train[val_idx]

        model.fit(X_train_fold, y_train_fold)
        y_pred = model.predict(X_val_fold)
        step_accuracy = accuracy_score(y_val_fold, y_pred)
        accuracy.append(step_accuracy)
        trial.report(step_accuracy, step)

        if trial.should_prune():
            raise optuna.exceptions.TrialPruned()

    return np.mean(accuracy)

mlflow_callback = MLflowCallback(
    tracking_uri=mlflow.get_tracking_uri(),
    metric_name="accuracy",
)

study = optuna.create_study(direction="maximize", pruner=optuna.pruners.MedianPruner())
study.optimize(objective, n_trials=10, callbacks=[mlflow_callback])

best_params = study.best_params
best_model = RandomForestClassifier(
    n_estimators=best_params['n_estimators'],
    max_depth=best_params['max_depth'],
    min_samples_split=best_params['min_samples_split'],
    min_samples_leaf=best_params['min_samples_leaf'],
    bootstrap=best_params['bootstrap'],
    random_state=42
)
best_model.fit(X_train, y_train)

with mlflow.start_run(run_name="Best Model", nested=True):
    for param, value in best_params.items():
        mlflow.log_param(param, value)
    mlflow.sklearn.log_model(best_model, "model")
    mlflow.log_metrics({"accuracy": study.best_value})


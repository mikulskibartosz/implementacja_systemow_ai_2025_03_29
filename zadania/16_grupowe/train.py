import mlflow
import optuna
import pandas as pd
import numpy as np
import yaml
import os
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.model_selection import KFold
from optuna.integration.mlflow import MLflowCallback
from sklearn.metrics import f1_score, precision_score, recall_score

with open('params.yaml', 'r') as f:
    params = yaml.safe_load(f)

optuna_params = params['optuna']

X_train = pd.read_csv('data/x_train.csv')
y_train = pd.read_csv('data/y_train.csv')
X_test = pd.read_csv('data/x_test.csv')
y_test = pd.read_csv('data/y_test.csv')

y_train = y_train.values.ravel()
y_test = y_test.values.ravel()

cv = KFold(n_splits=5, shuffle=True, random_state=42)

def objective(trial):
    n_estimators = trial.suggest_int(
        'n_estimators',
        optuna_params['n_estimators']['min'],
        optuna_params['n_estimators']['max'],
        step=optuna_params['n_estimators']['step']
    )
    learning_rate = trial.suggest_float(
        'learning_rate',
        optuna_params['learning_rate']['min'],
        optuna_params['learning_rate']['max'],
        log=optuna_params['learning_rate']['log']
    )
    max_depth = trial.suggest_int(
        'max_depth',
        optuna_params['max_depth']['min'],
        optuna_params['max_depth']['max']
    )
    min_samples_split = trial.suggest_int(
        'min_samples_split',
        optuna_params['min_samples_split']['min'],
        optuna_params['min_samples_split']['max']
    )
    min_samples_leaf = trial.suggest_int(
        'min_samples_leaf',
        optuna_params['min_samples_leaf']['min'],
        optuna_params['min_samples_leaf']['max']
    )
    subsample = trial.suggest_float(
        'subsample',
        optuna_params['subsample']['min'],
        optuna_params['subsample']['max']
    )

    model = GradientBoostingClassifier(
        n_estimators=n_estimators,
        learning_rate=learning_rate,
        max_depth=max_depth,
        min_samples_split=min_samples_split,
        min_samples_leaf=min_samples_leaf,
        subsample=subsample,
        random_state=42
    )

    val_scores = []
    for step, (train_idx, val_idx) in enumerate(cv.split(X_train, y_train)):
        X_train_cv, X_val_cv = X_train.iloc[train_idx], X_train.iloc[val_idx]
        y_train_cv, y_val_cv = y_train[train_idx], y_train[val_idx]

        model.fit(X_train_cv, y_train_cv)
        val_score = model.score(X_val_cv, y_val_cv)
        val_scores.append(val_score)
        trial.report(val_score, step)

        if trial.should_prune():
            raise optuna.exceptions.TrialPruned()

    return np.mean(val_scores)

mlflow_callback = MLflowCallback(
    tracking_uri=mlflow.get_tracking_uri(),
    metric_name="accuracy"
)

study = optuna.create_study(
    study_name="ChurnClassifier",
    direction='maximize',
    pruner=optuna.pruners.MedianPruner()
)

study.optimize(objective, n_trials=optuna_params['trials'], callbacks=[mlflow_callback])

best_params = study.best_params
best_model = GradientBoostingClassifier(
    n_estimators=best_params['n_estimators'],
    learning_rate=best_params['learning_rate'],
    max_depth=best_params['max_depth'],
    min_samples_split=best_params['min_samples_split'],
    min_samples_leaf=best_params['min_samples_leaf'],
    subsample=best_params['subsample'],
    random_state=42
)
best_model.fit(X_train, y_train)

with mlflow.start_run(run_name="Best Model", nested=True):
    for param, value in best_params.items():
        mlflow.log_param(f"best_{param}", value)

    mlflow.log_metric("best_score", study.best_value)

    y_pred = best_model.predict(X_test)
    test_score = best_model.score(X_test, y_test)
    mlflow.log_metric("test_score", test_score)

    f1 = f1_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred)
    recall = recall_score(y_test, y_pred)

    mlflow.log_metric("f1_score", f1)
    mlflow.log_metric("precision", precision)
    mlflow.log_metric("recall", recall)

    print("best_test_score", test_score)
    print("best_f1_score", f1)
    print("best_precision", precision)
    print("best_recall", recall)

    example_input = X_train.iloc[:5]
    example_output = best_model.predict(example_input)

    signature = mlflow.models.infer_signature(
        example_input,
        example_output
    )

    mlflow.sklearn.log_model(
        best_model,
        "best_model",
        signature=signature,
        input_example=example_input
    )

    current_file = os.path.abspath(__file__)
    mlflow.log_artifact(current_file)

    mlflow.register_model(
        f"runs:/{mlflow.active_run().info.run_id}/best_model",
        "ChurnClassifier"
    )

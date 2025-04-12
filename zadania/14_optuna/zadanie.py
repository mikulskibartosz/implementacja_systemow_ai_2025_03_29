import mlflow
import optuna
from sklearn.datasets import fetch_openml
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split, KFold
from optuna.integration.mlflow import MLflowCallback
import pandas as pd
from sklearn.preprocessing import OneHotEncoder
import os
import pickle


print("Wczytywanie zbioru Palmer Penguins...")
df = fetch_openml(data_id=42585)
df = df['frame']
df = df.dropna()
print(f"Wczytano dane. Kształt zbioru: {df.shape}")
print(f"Kolumny: {df.columns}")

X = df.drop(columns=['species'])
y = df['species']
print(f"Podział na zmienne: X shape: {X.shape}, y shape: {y.shape}")

print("Wykonywanie one-hot encoding...")
encoder = OneHotEncoder(sparse_output=False, handle_unknown='ignore')
X_categorical = X[['sex', 'island']].copy()
X_numerical = X.drop(columns=['sex', 'island']).copy()

encoded_features = encoder.fit_transform(X_categorical)
encoded_feature_names = encoder.get_feature_names_out(['sex', 'island'])

encoded_df = pd.DataFrame(encoded_features, columns=encoded_feature_names, index=X.index)
encoded_df = pd.concat([X_numerical, encoded_df], axis=1)
print(f"Zakończono encoding. Nowy kształt danych: {encoded_df.shape}")

encoder_path = "encoder.pkl"
with open(encoder_path, "wb") as f:
    pickle.dump(encoder, f)

print("Podział na zbiór treningowy i testowy...")
X_train, X_test, y_train, y_test = train_test_split(encoded_df, y, test_size=0.2, random_state=42)
print(f"Zbiór treningowy: {X_train.shape}, Zbiór testowy: {X_test.shape}")

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

    for step, (train_idx, val_idx) in enumerate(cv.split(X_train, y_train)):
        X_train_cv, X_val_cv = X_train.iloc[train_idx], X_train.iloc[val_idx]
        y_train_cv, y_val_cv = y_train.iloc[train_idx], y_train.iloc[val_idx]

        model.fit(X_train_cv, y_train_cv)
        val_score = model.score(X_val_cv, y_val_cv)

        trial.report(val_score, step)

        if trial.should_prune():
            raise optuna.exceptions.TrialPruned()

    return val_score

mlflow_callback = MLflowCallback(
    tracking_uri=mlflow.get_tracking_uri(),
    metric_name="accuracy"
)

study = optuna.create_study(
    direction='maximize',
    pruner=optuna.pruners.MedianPruner()
)

study.optimize(objective, n_trials=20, callbacks=[mlflow_callback])

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
        mlflow.log_param(f"best_{param}", value)

    mlflow.log_metric("best_score", study.best_value)

    y_pred = best_model.predict(X_test)
    test_score = best_model.score(X_test, y_test)
    mlflow.log_metric("test_score", test_score)

    mlflow.sklearn.log_model(best_model, "best_model")

    mlflow.log_artifact(encoder_path)

    current_file = os.path.abspath(__file__)
    mlflow.log_artifact(current_file)

    mlflow.register_model(
        f"runs:/{mlflow.active_run().info.run_id}/best_model",
        "PenguinsClassifier"
    )

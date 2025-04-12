import mlflow
import mlflow.sklearn
from sklearn.datasets import fetch_openml
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
import pandas as pd
from mlflow.models.signature import infer_signature
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

mlflow.set_experiment("Palmer Penguins-Klasyfikacja")

param_sets = [
    {"n_estimators": 50, "max_depth": 5, "min_samples_split": 2, "random_state": 42},
    {"n_estimators": 100, "max_depth": 10, "min_samples_split": 2, "random_state": 42},
    {"n_estimators": 200, "max_depth": 15, "min_samples_split": 5, "random_state": 42},
    {"n_estimators": 100, "max_depth": None, "min_samples_split": 10, "random_state": 42},
    {"n_estimators": 150, "max_depth": 8, "min_samples_split": 3, "random_state": 42}
]

for i, params in enumerate(param_sets):
    with mlflow.start_run(run_name=f"RandomForest-Run-{i+1}"):
        print(f"\nEksperyment {i+1} z parametrami: {params}")

        for param_name, param_value in params.items():
            mlflow.log_param(param_name, param_value)

        mlflow.log_param("dataset", "Palmer Penguins")
        mlflow.log_param("model_type", "RandomForestClassifier")

        model = RandomForestClassifier(**params)
        model.fit(X_train, y_train)

        y_pred = model.predict(X_test)
        accuracy = accuracy_score(y_test, y_pred)
        precision = precision_score(y_test, y_pred, average='weighted')
        recall = recall_score(y_test, y_pred, average='weighted')
        f1 = f1_score(y_test, y_pred, average='weighted')

        mlflow.log_metric("accuracy", accuracy)
        mlflow.log_metric("precision", precision)
        mlflow.log_metric("recall", recall)
        mlflow.log_metric("f1_score", f1)

        signature = infer_signature(X_train, model.predict(X_train))

        mlflow.sklearn.log_model(
            model,
            "model",
            signature=signature,
            input_example=X_train[:5]
        )

        mlflow.log_artifact(encoder_path)

        current_file = os.path.abspath(__file__)
        mlflow.log_artifact(current_file)


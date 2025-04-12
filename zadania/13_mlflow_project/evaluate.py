import argparse
import mlflow
import mlflow.sklearn
from sklearn.datasets import fetch_openml
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
import pandas as pd
import pickle
import os

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--run-id", type=str, required=True)
    return parser.parse_args()

def main():
    args = parse_args()

    print("Wczytywanie zbioru Palmer Penguins...")
    df = fetch_openml(data_id=42585)
    df = df['frame']
    df = df.dropna()
    print(f"Wczytano dane. Kształt zbioru: {df.shape}")
    print(f"Kolumny: {df.columns}")

    X = df.drop(columns=['species'])
    y = df['species']
    print(f"Podział na zmienne: X shape: {X.shape}, y shape: {y.shape}")

    print(f"Pobieranie encodera z run_id: {args.run_id}")
    client = mlflow.tracking.MlflowClient()
    artifact_path = client.download_artifacts(args.run_id, "encoder.pkl", ".")

    with open(artifact_path, "rb") as f:
        encoder = pickle.load(f)

    print("Przetwarzanie danych z użyciem zapisanego encodera...")
    X_categorical = X[['sex', 'island']].copy()
    X_numerical = X.drop(columns=['sex', 'island']).copy()

    encoded_features = encoder.transform(X_categorical)
    encoded_feature_names = encoder.get_feature_names_out(['sex', 'island'])

    encoded_df = pd.DataFrame(encoded_features, columns=encoded_feature_names, index=X.index)
    encoded_df = pd.concat([X_numerical, encoded_df], axis=1)
    print(f"Zakończono encoding. Nowy kształt danych: {encoded_df.shape}")

    print("Podział na zbiór treningowy i testowy...")
    X_train, X_test, y_train, y_test = train_test_split(encoded_df, y, test_size=0.2, random_state=42)
    print(f"Zbiór treningowy: {X_train.shape}, Zbiór testowy: {X_test.shape}")

    print(f"Ładowanie modelu z run_id: {args.run_id}")
    model = mlflow.sklearn.load_model(f"runs:/{args.run_id}/model")

    y_pred = model.predict(X_test)

    accuracy = accuracy_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred, average='weighted')
    recall = recall_score(y_test, y_pred, average='weighted')
    f1 = f1_score(y_test, y_pred, average='weighted')

    print(f"\nWyniki ewaluacji modelu:")
    print(f"Dokładność: {accuracy:.4f}")
    print(f"Precyzja: {precision:.4f}")
    print(f"Czułość: {recall:.4f}")
    print(f"F1-score: {f1:.4f}")

if __name__ == "__main__":
    main()
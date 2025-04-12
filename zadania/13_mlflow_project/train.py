import argparse
import mlflow
import mlflow.sklearn
from sklearn.datasets import fetch_openml
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import OneHotEncoder
import pandas as pd
from mlflow.models.signature import infer_signature
import os
import pickle

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--n-estimators", type=int, default=100)
    parser.add_argument("--max-depth", type=int, default=5)
    parser.add_argument("--random-state", type=int, default=42)
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
    X_train, X_test, y_train, y_test = train_test_split(encoded_df, y, test_size=0.2, random_state=args.random_state)
    print(f"Zbiór treningowy: {X_train.shape}, Zbiór testowy: {X_test.shape}")

    with mlflow.start_run():
        mlflow.log_param("n_estimators", args.n_estimators)
        mlflow.log_param("max_depth", args.max_depth)
        mlflow.log_param("random_state", args.random_state)
        mlflow.log_param("dataset", "Palmer Penguins")
        mlflow.log_param("model_type", "RandomForestClassifier")

        model = RandomForestClassifier(
            n_estimators=args.n_estimators,
            max_depth=args.max_depth,
            random_state=args.random_state
        )
        model.fit(X_train, y_train)

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

        print(f"Run ID: {mlflow.active_run().info.run_id}")

if __name__ == "__main__":
    main()
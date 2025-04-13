import os
import yaml
import pandas as pd
import pickle
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report

def train_model():
    with open("params.yaml", "r") as f:
        params = yaml.safe_load(f)

    data_path = params.get("download", {}).get("output_path", "data/dataset.csv")

    model_params = params.get("train", {})
    test_size = model_params.get("test_size", 0.2)
    random_state = model_params.get("random_state", 42)
    max_depth = model_params.get("max_depth", None)

    print(f"Loading dataset from {data_path}")
    df = pd.read_csv(data_path)

    X = df.drop('species', axis=1)
    y = df['species']

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=random_state
    )

    print(f"Training with {X_train.shape[0]} samples, testing with {X_test.shape[0]} samples")

    model = DecisionTreeClassifier(max_depth=max_depth, random_state=random_state)
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)

    print(f"Model accuracy: {accuracy:.4f}")
    print("\nClassification Report:")
    print(classification_report(y_test, y_pred))

    os.makedirs("models", exist_ok=True)
    with open("models/model.pkl", "wb") as f:
        pickle.dump(model, f)

    with open("metrics.json", "w") as f:
        import json
        json.dump({"accuracy": accuracy}, f)

    print("Model saved to models/model.pkl")
    print("Metrics saved to metrics.json")

if __name__ == "__main__":
    train_model()

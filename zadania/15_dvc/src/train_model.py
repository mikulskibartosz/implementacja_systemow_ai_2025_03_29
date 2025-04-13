import pandas as pd
import yaml
import os
import json
import pickle
import mlflow
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

with open("params.yaml", "r") as f:
    params = yaml.safe_load(f)

train_path = params.get("prepare", {}).get("train_path", "data/train.csv")
test_path = params.get("prepare", {}).get("test_path", "data/test.csv")
encoder_path = params.get("prepare", {}).get("one_hot_encoding", {}).get("encoder_path", "models/encoder.pkl")
model_path = params.get("train", {}).get("model_path", "models/model.pkl")

model_params = params.get("train", {}).get("model", {})
n_estimators = model_params.get("n_estimators", 100)
max_depth = model_params.get("max_depth", None)
min_samples_split = model_params.get("min_samples_split", 2)
min_samples_leaf = model_params.get("min_samples_leaf", 1)
bootstrap = model_params.get("bootstrap", True)
random_state = model_params.get("random_state", 42)

print(f"Loading training data from {train_path}...")
train_df = pd.read_csv(train_path)
print(f"Loading test data from {test_path}...")
test_df = pd.read_csv(test_path)

X_train = train_df.drop(columns=['species'])
y_train = train_df['species']
X_test = test_df.drop(columns=['species'])
y_test = test_df['species']

print(f"Training data shape: X={X_train.shape}, y={y_train.shape}")
print(f"Test data shape: X={X_test.shape}, y={y_test.shape}")

print("Training RandomForestClassifier...")
model = RandomForestClassifier(
    n_estimators=n_estimators,
    max_depth=max_depth,
    min_samples_split=min_samples_split,
    min_samples_leaf=min_samples_leaf,
    bootstrap=bootstrap,
    random_state=random_state
)

model.fit(X_train, y_train)

print("Evaluating model...")
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Test accuracy: {accuracy:.4f}")
print("\nClassification Report:")
print(classification_report(y_test, y_pred))

metrics = {
    "accuracy": float(accuracy)
}

with open("metrics.json", "w") as f:
    json.dump(metrics, f, indent=4)
print("Metrics saved to metrics.json")

os.makedirs(os.path.dirname(model_path), exist_ok=True)
with open(model_path, "wb") as f:
    pickle.dump(model, f)
print(f"Model saved to {model_path}")

mlflow_tracking_uri = params.get("train", {}).get("mlflow", {}).get("tracking_uri", "")
experiment_name = params.get("train", {}).get("mlflow", {}).get("experiment_name", "penguin_classification")

if mlflow_tracking_uri:
    mlflow.set_tracking_uri(mlflow_tracking_uri)

mlflow.set_experiment(experiment_name)

with mlflow.start_run(run_name="penguin_classifier"):
    mlflow.log_param("n_estimators", n_estimators)
    mlflow.log_param("max_depth", max_depth)
    mlflow.log_param("min_samples_split", min_samples_split)
    mlflow.log_param("min_samples_leaf", min_samples_leaf)
    mlflow.log_param("bootstrap", bootstrap)
    mlflow.log_param("random_state", random_state)

    mlflow.log_metric("accuracy", accuracy)

    mlflow.sklearn.log_model(model, "model")

    mlflow.log_artifact(encoder_path)

    model_name = params.get("train", {}).get("mlflow", {}).get("model_name", "PenguinsClassifier")
    mlflow.register_model(
        f"runs:/{mlflow.active_run().info.run_id}/model",
        model_name
    )

print("Training and evaluation completed successfully!")

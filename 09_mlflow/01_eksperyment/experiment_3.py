import mlflow
import mlflow.sklearn
import mlflow.data
from mlflow.data.pandas_dataset import PandasDataset
from mlflow.models.signature import infer_signature

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import pandas as pd
import numpy as np

iris = load_iris()
X = iris.data
y = iris.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

mlflow.set_experiment("Iris Classification")

with mlflow.start_run():
    n_estimators = 10
    max_depth = 1
    random_state = 42

    mlflow.log_params({
        "n_estimators": n_estimators,
        "max_depth": max_depth,
        "random_state": random_state
    })

    model = RandomForestClassifier(n_estimators=n_estimators, max_depth=max_depth, random_state=random_state)
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)

    mlflow.log_metrics({
        "accuracy": accuracy
    })

    signature = infer_signature(X_train, model.predict(X_train))

    mlflow.sklearn.log_model(
        model,
        "random_forest_model",
        signature=signature,
        input_example=X_train[:5]
    )

    iris_df = pd.DataFrame(data=np.c_[iris.data, iris.target], columns=iris.feature_names + ['target'])

    dataset: PandasDataset = mlflow.data.from_pandas(iris_df, source="iris_data.csv")
    mlflow.log_input(dataset, "iris_data")

    iris_csv_path = "iris_data.csv"
    iris_df.to_csv(iris_csv_path, index=False)

    mlflow.log_artifact(iris_csv_path, "data")

    mlflow.set_tag("model_type", "RandomForestClassifier")
    mlflow.set_tag("library", "sklearn")

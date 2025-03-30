import numpy as np
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
import joblib
import os

def train_model():
    iris = load_iris()
    X = iris.data
    y = iris.target

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = DecisionTreeClassifier(random_state=42)
    model.fit(X_train, y_train)

    score = model.score(X_test, y_test)
    print(f"Model accuracy score: {score:.4f}")

    os.makedirs("kalkulator/models", exist_ok=True)

    model_path = "kalkulator/models/iris_model.joblib"
    joblib.dump(model, model_path)
    print(f"Model saved to {model_path}")

    return model

# PAMIĘTAĆ O DODANIU __init__.py w folderze models!!!
if __name__ == "__main__":
    train_model()

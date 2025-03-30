from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
import bentoml

def train_model():
    iris = load_iris()
    X = iris.data
    y = iris.target

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = DecisionTreeClassifier(random_state=42)
    model.fit(X_train, y_train)

    score = model.score(X_test, y_test)
    print(f"Model accuracy score: {score:.4f}")

    model_tag = bentoml.sklearn.save_model(
    "iris_classifier",
    model,
    signatures={
        "predict": {"batchable": True, "batch_dim": 0},
        "predict_proba": {"batchable": True, "batch_dim": 0}
    },
    metadata={"accuracy": model.score(X_test, y_test)}
)

    print(f"Model zapisany: {model_tag}")

if __name__ == "__main__":
    train_model()

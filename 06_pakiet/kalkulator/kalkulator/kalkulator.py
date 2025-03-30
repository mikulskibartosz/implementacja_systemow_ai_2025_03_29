import joblib
import importlib.resources as pkg_resources
from . import models

def add(a, b):
    """Dodaje dwie liczby."""
    return a + b

def subtract(a, b):
    """Odejmuje b od a."""
    return a - b

def multiply(a, b):
    """Mnoży dwie liczby."""
    return a * b

def divide(a, b):
    """Dzieli a przez b."""
    if b == 0:
        raise ValueError("Nie można dzielić przez zero!")
    return a / b

def load_model():
    with pkg_resources.path(models, "iris_model.joblib") as model_path:
        model = joblib.load(model_path)
        return model

def predict(features):
    model = load_model()
    return model.predict(features)


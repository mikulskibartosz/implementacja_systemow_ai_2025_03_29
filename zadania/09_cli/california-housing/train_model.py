import numpy as np
import pandas as pd
import joblib
import os
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score

os.makedirs("california_housing/models", exist_ok=True)

print("Ładowanie zbioru danych California Housing...")
housing = fetch_california_housing()
X = pd.DataFrame(housing.data, columns=housing.feature_names)
y = housing.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
print(f"Rozmiar zbioru treningowego: {X_train.shape[0]}")
print(f"Rozmiar zbioru testowego: {X_test.shape[0]}")

print("Trenowanie modelu Random Forest Regressor...")
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print(f"Średni błąd kwadratowy: {mse:.4f}")
print(f"Współczynnik R²: {r2:.4f}")

model_path = "california_housing/models/model.joblib"
print(f"Zapisywanie modelu do {model_path}...")
joblib.dump(model, model_path)
print("Trening i zapisywanie modelu zakończone pomyślnie!")

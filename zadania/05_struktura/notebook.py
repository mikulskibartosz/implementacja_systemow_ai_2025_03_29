import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import pickle
import os

# podział na funkcję albo na skrypty
# pobieranie danych w osobnym pliku
# parametry modelu i podziału danych w konfiguracji
# wersje bibliotek w osobnym pliku
# użycie scikit-learn zamiast ręcznych obliczeń
# dokumentacja
# ścieżki danych wyjściowych w konfiguracji
# weryfikacja danych wejściowych
# obsługa błędów
# brak możliwości testowania
# logger zamiast printów
# random_state w konfiguracji

print("Ładowanie danych Iris...")
iris = load_iris()
X = iris.data
y = iris.target
feature_names = iris.feature_names
target_names = iris.target_names

print("Przygotowanie danych...")
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

print("Przetwarzanie danych...")
X_train_processed = X_train.copy()
X_test_processed = X_test.copy()

for i in range(4):
    mean = X_train[:, i].mean()
    std = X_train[:, i].std()
    X_train_processed[:, i] = (X_train[:, i] - mean) / std
    X_test_processed[:, i] = (X_test[:, i] - mean) / std

print("Trenowanie modelu...")
model = DecisionTreeClassifier(max_depth=3, random_state=42)
model.fit(X_train_processed, y_train)

print("Ewaluacja modelu...")
predictions = model.predict(X_test_processed)
accuracy = accuracy_score(y_test, predictions)
conf_matrix = confusion_matrix(y_test, predictions)
classification_rep = classification_report(y_test, predictions, target_names=target_names)

print("Zapisywanie modelu...")
with open('iris_model.pkl', 'wb') as file:
    pickle.dump(model, file)

print("Generowanie raportu...")
report_content = f"""RAPORT Z TRENINGU MODELU
============================================
Dokładność: {accuracy * 100:.2f}%

Macierz pomyłek:
{conf_matrix}

Raport klasyfikacji:
{classification_rep}

Model zapisany jako: iris_model.pkl
"""

with open('model_report.txt', 'w') as file:
    file.write(report_content)

print("Wizualizacja wyników...")
fig, axs = plt.subplots(2, 2, figsize=(12, 10))
plt.suptitle(f'Analiza modelu Iris (Dokładność: {accuracy:.2f})')

feature_pairs = [(0, 1), (2, 3), (0, 2), (1, 3)]
for idx, (i, j) in enumerate(feature_pairs):
    row, col = idx // 2, idx % 2

    axs[row, col].scatter(X_test_processed[:, i], X_test_processed[:, j], c=predictions,
                          cmap='viridis', edgecolor='k', s=70, alpha=0.7)
    axs[row, col].scatter(X_test_processed[:, i], X_test_processed[:, j],
                         c=y_test,
                         cmap='viridis',
                         marker='x',
                         label='True Values',
                         s=70, alpha=0.7)
    axs[row, col].set_xlabel(feature_names[i])
    axs[row, col].set_ylabel(feature_names[j])
    axs[row, col].set_title(f'Cechy: {feature_names[i]} vs {feature_names[j]}')

plt.tight_layout()
plt.subplots_adjust(top=0.9)
plt.savefig('iris_visualization.png')

print(f"\nWyniki treningu:")
print(f"Dokładność: {accuracy * 100:.2f}%")
print(f"Model zapisany jako: iris_model.pkl")
print(f"Raport zapisany jako: model_report.txt")
print(f"Wizualizacja zapisana jako: iris_visualization.png")
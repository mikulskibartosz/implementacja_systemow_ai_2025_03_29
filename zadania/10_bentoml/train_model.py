import bentoml
from sklearn.datasets import fetch_openml
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
import pandas as pd


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

print("Podział na zbiór treningowy i testowy...")
X_train, X_test, y_train, y_test = train_test_split(encoded_df, y, test_size=0.2, random_state=42)
print(f"Zbiór treningowy: {X_train.shape}, Zbiór testowy: {X_test.shape}")

print("Trenowanie modelu...")
model = DecisionTreeClassifier()
model.fit(X_train, y_train)
accuracy = model.score(X_test, y_test)
print(f"Model wytrenowany. Dokładność: {accuracy:.4f}")

print("Zapisywanie encodera w BentoML...")
encoder_tag = bentoml.sklearn.save_model(
    "penguins_encoder",
    encoder,
    signatures={
        "transform": {"batchable": True, "batch_dim": 0},
    },
    metadata={"description": "OneHotEncoder for sex and island features"}
)
print(f"Encoder zapisany w BentoML: {encoder_tag}")

print("Zapisywanie modelu w BentoML...")
model_tag = bentoml.sklearn.save_model(
    "penguins_classifier",
    model,
    signatures={
        "predict": {"batchable": True, "batch_dim": 0},
    },
    metadata={"accuracy": accuracy}
)

print(f"Model zapisany: {model_tag}")

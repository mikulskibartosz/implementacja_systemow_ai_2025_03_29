import pandas as pd
import yaml
import os
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
import pickle

with open("params.yaml", "r") as f:
    params = yaml.safe_load(f)

input_path = params.get("download", {}).get("output_path", "data/dataset.csv")
train_path = params.get("prepare", {}).get("train_path", "data/train.csv")
test_path = params.get("prepare", {}).get("test_path", "data/test.csv")
one_hot_columns = params.get("prepare", {}).get("one_hot_encoding", {}).get("columns", [])
encoder_path = params.get("prepare", {}).get("one_hot_encoding", {}).get("encoder_path", "models/encoder.pkl")
split_params = params.get("prepare", {}).get("split", {})
test_size = split_params.get("test_size", 0.2)
random_state = split_params.get("random_state", 42)

os.makedirs(os.path.dirname(train_path), exist_ok=True)
os.makedirs(os.path.dirname(test_path), exist_ok=True)

print(f"Loading dataset from {input_path}...")
df = pd.read_csv(input_path)
df = df.dropna()
print(f"Loaded data. Shape: {df.shape}")
print(f"Columns: {df.columns}")

X = df.drop(columns=['species'])
y = df['species']
print(f"Features shape: {X.shape}, Target shape: {y.shape}")

print(f"Performing one-hot encoding on columns: {one_hot_columns}")
encoder = OneHotEncoder(sparse_output=False, handle_unknown='ignore')
X_categorical = X[one_hot_columns].copy()
X_numerical = X.drop(columns=one_hot_columns).copy()

encoded_features = encoder.fit_transform(X_categorical)
encoded_feature_names = encoder.get_feature_names_out(one_hot_columns)

encoded_df = pd.DataFrame(encoded_features, columns=encoded_feature_names, index=X.index)
X_processed = pd.concat([X_numerical, encoded_df], axis=1)
print(f"Encoding completed. New data shape: {X_processed.shape}")

os.makedirs(os.path.dirname(encoder_path), exist_ok=True)
with open(encoder_path, "wb") as f:
    pickle.dump(encoder, f)
print(f"Encoder saved to {encoder_path}")

print("Splitting into training and test sets...")
X_train, X_test, y_train, y_test = train_test_split(X_processed, y, test_size=test_size, random_state=random_state)
print(f"Training set: {X_train.shape}, Test set: {X_test.shape}")

train_df = pd.concat([X_train, y_train], axis=1)
test_df = pd.concat([X_test, y_test], axis=1)

train_df.to_csv(train_path, index=False)
test_df.to_csv(test_path, index=False)
print(f"Training data saved to {train_path}")
print(f"Test data saved to {test_path}")

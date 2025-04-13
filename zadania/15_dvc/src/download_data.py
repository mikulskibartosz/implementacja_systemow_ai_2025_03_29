from sklearn.datasets import fetch_openml
import yaml

with open("params.yaml", "r") as f:
    params = yaml.safe_load(f)

output_path = params.get("download", {}).get("output_path", "data/dataset.csv")

df = fetch_openml(data_id=42585)
df = df['frame']
df = df.dropna()
print(f"Wczytano dane. Kształt zbioru: {df.shape}")
print(f"Kolumny: {df.columns}")

df.to_csv(output_path, index=False)

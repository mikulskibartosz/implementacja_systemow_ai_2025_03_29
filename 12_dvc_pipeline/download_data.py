import os
import yaml
import pandas as pd
from sklearn.datasets import load_iris

def download_iris_dataset(output_path):
    """
    Download the Iris dataset and save it to the specified path.

    Args:
        output_path (str): Path where the dataset will be saved
    """
    print("Downloading Iris dataset...")
    iris = load_iris()


    df = pd.DataFrame(data=iris.data, columns=iris.feature_names)

    df['species'] = pd.Categorical.from_codes(iris.target, iris.target_names)

    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    df.to_csv(output_path, index=False)
    print(f"Dataset saved to {output_path}")
    print(f"Dataset shape: {df.shape}")
    print(f"Columns: {df.columns.tolist()}")

def main():
    with open("params.yaml", "r") as f:
        params = yaml.safe_load(f)

    output_path = params.get("download", {}).get("output_path", "data/dataset.csv")

    download_iris_dataset(output_path)

if __name__ == "__main__":
    main()

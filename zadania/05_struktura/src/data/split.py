import pandas as pd
from pathlib import Path
from sklearn.model_selection import train_test_split
import click
from src.utils.logger import setup_logger
from src.utils.config import load_config


def split_data(config):
    logger = setup_logger()

    if config is None:
        raise ValueError("Konfiguracja jest None")

    test_size = config.split.test_size
    random_state = config.split.random_state
    input_path = config.split.input.raw_path
    output_train_path = config.split.output.train_path
    output_test_path = config.split.output.test_path

    if not input_path.exists():
        raise ValueError(f"Plik wejściowy nie istnieje: {input_path}")

    if output_train_path.exists():
        raise ValueError(f"Plik wyjściowy już istnieje: {output_train_path}")

    if output_test_path.exists():
        raise ValueError(f"Plik wyjściowy już istnieje: {output_test_path}")

    logger.info(f"Wczytywanie danych z {input_path}...")
    df = pd.read_csv(input_path)

    X = df.drop("target", axis=1).values
    y = df["target"].values
    feature_names = df.drop("target", axis=1).columns.tolist()

    logger.info("Dzielenie danych na zbiory treningowy i testowy...")
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=random_state
    )

    # Tworzenie katalogów nadrzędnych, jeśli nie istnieją
    output_train_path.parent.mkdir(parents=True, exist_ok=True)
    output_test_path.parent.mkdir(parents=True, exist_ok=True)

    logger.info(f"Zapisywanie danych treningowych do {output_train_path}")
    train_df = pd.DataFrame(X_train, columns=feature_names)
    train_df["target"] = y_train
    train_df.to_csv(output_train_path, index=False)

    logger.info(f"Zapisywanie danych testowych do {output_test_path}")
    test_df = pd.DataFrame(X_test, columns=feature_names)
    test_df["target"] = y_test
    test_df.to_csv(output_test_path, index=False)

    logger.info("Dane zostały podzielone i zapisane pomyślnie")


@click.command()
@click.option(
    "--config-path", type=str, default=None, help="Ścieżka do pliku konfiguracyjnego"
)
def main(config_path):
    config = load_config(config_path)
    split_data(config)


if __name__ == "__main__":
    main()

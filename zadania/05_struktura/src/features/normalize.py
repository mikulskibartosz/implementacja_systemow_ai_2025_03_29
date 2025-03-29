import pandas as pd
import click
from sklearn.preprocessing import StandardScaler
from src.utils.logger import setup_logger
from src.utils.config import load_config


def normalize_data(config):
    logger = setup_logger()

    if config is None:
        raise ValueError("Config jest None")

    input_train_path = config.normalize.input.train_path
    input_test_path = config.normalize.input.test_path
    output_train_path = config.normalize.output.train_path
    output_test_path = config.normalize.output.test_path
    skip_columns = config.normalize.skip_columns

    if not input_train_path.exists():
        raise ValueError(f"Plik treningowy wejściowy nie istnieje: {input_train_path}")

    if not input_test_path.exists():
        raise ValueError(f"Plik testowy wejściowy nie istnieje: {input_test_path}")

    if output_train_path.exists():
        raise ValueError(f"Plik treningowy wyjściowy już istnieje: {output_train_path}")

    if output_test_path.exists():
        raise ValueError(f"Plik testowy wyjściowy już istnieje: {output_test_path}")

    logger.info(f"Ładowanie danych treningowych z {input_train_path}...")
    train_df = pd.read_csv(input_train_path)

    logger.info(f"Ładowanie danych testowych z {input_test_path}...")
    test_df = pd.read_csv(input_test_path)

    features_to_normalize = [col for col in train_df.columns if col not in skip_columns]
    X_train = train_df[features_to_normalize]
    X_test = test_df[features_to_normalize]

    skipped_columns_train = {col: train_df[col] for col in skip_columns}
    skipped_columns_test = {col: test_df[col] for col in skip_columns}

    logger.info(f"Normalizacja danych przy użyciu StandardScaler (pomijając kolumny: {skip_columns})...")
    scaler = StandardScaler()
    X_train_normalized = scaler.fit_transform(X_train)
    X_test_normalized = scaler.transform(X_test)


    output_train_path.parent.mkdir(parents=True, exist_ok=True)
    output_test_path.parent.mkdir(parents=True, exist_ok=True)

    logger.info(f"Zapisywanie znormalizowanych danych treningowych do {output_train_path}")
    train_normalized_df = pd.DataFrame(X_train_normalized, columns=features_to_normalize)

    for col, values in skipped_columns_train.items():
        train_normalized_df[col] = values
    train_normalized_df.to_csv(output_train_path, index=False)

    logger.info(f"Zapisywanie znormalizowanych danych testowych do {output_test_path}")
    test_normalized_df = pd.DataFrame(X_test_normalized, columns=features_to_normalize)

    for col, values in skipped_columns_test.items():
        test_normalized_df[col] = values

    test_normalized_df.to_csv(output_test_path, index=False)

    logger.info("Normalizacja danych zakończona pomyślnie")


@click.command()
@click.option(
    "--config-path", type=str, default=None, help="Ścieżka do pliku konfiguracyjnego"
)
def main(config_path):
    config = load_config(config_path)
    normalize_data(config)


if __name__ == "__main__":
    main()

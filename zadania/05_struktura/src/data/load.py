from sklearn.datasets import load_iris
import pandas as pd
import click
from src.utils.logger import setup_logger
from src.utils.config import load_config


def load_data(config):
    logger = setup_logger()

    if config is None:
        raise ValueError("Config jest None")

    output_raw_path = config.load.output_raw_path

    if output_raw_path.exists():
        raise ValueError(f"Plik wyjściowy już istnieje: {output_raw_path}")

    logger.info("Ładowanie zbioru danych Iris...")
    iris = load_iris()
    X = iris.data
    y = iris.target
    feature_names = iris.feature_names

    output_raw_path.parent.mkdir(parents=True, exist_ok=True)

    logger.info(f"Zapisywanie surowych danych do {output_raw_path}")
    df = pd.DataFrame(X, columns=feature_names)
    df[config.load.target_column] = y
    df.to_csv(output_raw_path, index=False)

    logger.info("Surowe dane zostały pomyślnie zapisane")


@click.command()
@click.option(
    "--config-path", type=str, default=None, help="Ścieżka do pliku konfiguracyjnego"
)
def main(config_path):
    config = load_config(config_path)
    load_data(config)


if __name__ == "__main__":
    main()

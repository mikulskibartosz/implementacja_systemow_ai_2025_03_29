import pandas as pd
from sklearn.tree import DecisionTreeClassifier
import pickle
import click
from pathlib import Path
from src.utils.logger import setup_logger
from src.utils.config import load_config


def train_model(config):
    logger = setup_logger()

    if config is None:
        raise ValueError("Config jest None")

    model_name = config.train.model.name
    max_depth = config.train.model.max_depth
    random_state = config.train.model.random_state

    train_path = config.train.input.train_path
    output_model_path = config.train.output.output_model_path

    if not train_path.exists():
        raise ValueError(f"Plik danych treningowych nie istnieje: {train_path}")

    if Path(output_model_path).exists():
        raise FileExistsError(f"Plik modelu wyjściowego już istnieje: {output_model_path}")

    logger.info(f"Ładowanie znormalizowanych danych treningowych z {train_path}...")
    train_df = pd.read_csv(train_path)

    X_train = train_df.drop("target", axis=1).values
    y_train = train_df["target"].values

    logger.info(f"Trenowanie modelu {model_name}...")
    if model_name == "decision_tree":
        model = DecisionTreeClassifier(max_depth=max_depth, random_state=random_state)
    else:
        raise ValueError(f"Nieobsługiwany typ modelu: {model_name}")

    model.fit(X_train, y_train)

    logger.info("Trening modelu zakończony pomyślnie")

    output_dir = Path(output_model_path).parent
    output_dir.mkdir(parents=True, exist_ok=True)

    logger.info(f"Zapisywanie modelu do {output_model_path}...")
    try:
        with open(output_model_path, 'wb') as file:
            pickle.dump(model, file)
        logger.info("Model zapisany pomyślnie")
    except Exception as e:
        logger.error(f"Błąd podczas zapisywania modelu: {e}")
        raise


@click.command()
@click.option(
    "--config-path", type=str, default=None, help="Ścieżka do pliku konfiguracyjnego"
)
def main(config_path):
    config = load_config(config_path)
    train_model(config)


if __name__ == "__main__":
    main()

import pandas as pd
import pickle
import click
import matplotlib.pyplot as plt
from pathlib import Path
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from src.utils.logger import setup_logger
from src.utils.config import load_config


def evaluate_model(config):
    logger = setup_logger()

    if config is None:
        raise ValueError("Config jest None")

    test_path = config.evaluate.input.test_path
    model_path = config.evaluate.input.model_path
    report_path = config.evaluate.output.report_path
    graph_path = config.evaluate.output.graph_path

    if not test_path.exists():
        raise ValueError(f"Plik danych testowych nie istnieje: {test_path}")

    if not model_path.exists():
        raise ValueError(f"Plik modelu nie istnieje: {model_path}")

    Path(report_path).parent.mkdir(parents=True, exist_ok=True)
    Path(graph_path).parent.mkdir(parents=True, exist_ok=True)

    logger.info(f"Ładowanie danych testowych z {test_path}...")
    test_df = pd.read_csv(test_path)

    X_test = test_df.drop("target", axis=1).values
    y_test = test_df["target"].values

    feature_names = test_df.drop("target", axis=1).columns.tolist()

    logger.info(f"Ładowanie modelu z {model_path}...")
    try:
        with open(model_path, 'rb') as file:
            model = pickle.load(file)
    except Exception as e:
        logger.error(f"Błąd ładowania modelu: {e}")
        raise

    logger.info("Tworzenie predykcji...")
    predictions = model.predict(X_test)

    logger.info("Ocenianie wydajności modelu...")
    accuracy = accuracy_score(y_test, predictions)
    conf_matrix = confusion_matrix(y_test, predictions)
    classification_rep = classification_report(y_test, predictions)

    logger.info(f"Dokładność modelu: {accuracy:.4f}")

    logger.info(f"Generowanie raportu ewaluacji do {report_path}...")
    report_content = f"""RAPORT EWALUACJI
============================================
Dokładność: {accuracy * 100:.2f}%

Macierz pomyłek:
{conf_matrix}

Raport klasyfikacji:
{classification_rep}

Ścieżka modelu: {model_path}
"""

    try:
        with open(report_path, 'w') as file:
            file.write(report_content)
        logger.info("Raport zapisany pomyślnie")
    except Exception as e:
        logger.error(f"Błąd zapisywania raportu: {e}")
        raise

    logger.info(f"Generowanie wizualizacji ewaluacji do {graph_path}...")
    try:
        if X_test.shape[1] >= 2:
            fig, axs = plt.subplots(2, 2, figsize=(12, 10))
            plt.suptitle(f'Ewaluacja modelu (Dokładność: {accuracy:.4f})')

            feature_pairs = []
            for i in range(min(4, X_test.shape[1])):
                for j in range(i+1, min(4, X_test.shape[1])):
                    feature_pairs.append((i, j))
                    if len(feature_pairs) >= 4:
                        break
                if len(feature_pairs) >= 4:
                    break

            while len(feature_pairs) < 4:
                feature_pairs.append(feature_pairs[0])

            for idx, (i, j) in enumerate(feature_pairs[:4]):
                row, col = idx // 2, idx % 2

                axs[row, col].scatter(X_test[:, i], X_test[:, j], c=predictions,
                                    cmap='viridis', edgecolor='k', s=70, alpha=0.7)
                axs[row, col].scatter(X_test[:, i], X_test[:, j], c=y_test,
                                    cmap='viridis', marker='x', s=70, alpha=0.7)

                x_label = feature_names[i] if i < len(feature_names) else f"Cecha {i}"
                y_label = feature_names[j] if j < len(feature_names) else f"Cecha {j}"

                axs[row, col].set_xlabel(x_label)
                axs[row, col].set_ylabel(y_label)
                axs[row, col].set_title(f'{x_label} vs {y_label}')

            plt.tight_layout()
            plt.subplots_adjust(top=0.9)
            plt.savefig(graph_path)
            logger.info("Wizualizacja zapisana pomyślnie")
        else:
            logger.warning("Za mało cech do wizualizacji")
    except Exception as e:
        logger.error(f"Błąd tworzenia wizualizacji: {e}")

    logger.info("Ewaluacja modelu zakończona pomyślnie")


@click.command()
@click.option(
    "--config-path", type=str, default=None, help="Ścieżka do pliku konfiguracyjnego"
)
def main(config_path):
    config = load_config(config_path)
    evaluate_model(config)


if __name__ == "__main__":
    main()

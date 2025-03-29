import click

@click.command(help="Trenowanie modelu")
@click.argument("data", type=str, required=True)
@click.option("--data-path", type=str, required=True, help="Ścieżka do danych treningowych")
@click.option("-v", 'verbose', count=True, help="Włącza tryb wysyłania logów")
@click.option("--cache/--no-cache", default=True, help="Cache")
@click.option("--learning-rate", type=float, default=0.01, help="Learning rate")
@click.option("--features", type=str, multiple=True, default=[])
@click.version_option(version="0.1.0")
def train(data, data_path, verbose, cache, learning_rate, features):
    args = {
        "data": data,
        "data-path": data_path,
        "verbose": verbose,
        "cache": cache,
        "learning-rate": learning_rate,
        "features": features,
    }
    print("Args: ", args)


if __name__ == "__main__":
    train()

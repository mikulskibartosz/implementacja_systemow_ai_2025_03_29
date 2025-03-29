import click
import pandas as pd

@click.group()
def cli():
    """Aplikacja do konwertowania danych CSV."""
    pass

@cli.command(help="Zapisz dane do pliku JSON")
@click.option('--input', type=str, required=True,
              help='Ścieżka do pliku CSV')
@click.option('--output', type=str, required=True,
              help='Ścieżka do pliku wyjściowego JSON')
@click.option('--columns', multiple=True, default=None,
              help='Kolumny do zapisania (domyślnie wszystkie)')
@click.option('--rows', type=int, default=None,
              help='Liczba wierszy do zapisania (domyślnie wszystkie)')
@click.option('--orient', type=click.Choice(['records', 'columns', 'index', 'split', 'table']),
              default='records', help='Format JSON (domyślnie records)')
def to_json(input, output, columns, rows, orient):
    """Wczytaj dane z CSV i zapisz je jako JSON."""
    click.echo(f"Wczytuje dane z {input}...")
    df = pd.read_csv(input)

    if columns:
        selected_df = df[list(columns)]
    else:
        selected_df = df

    if rows is not None:
        selected_df = selected_df.head(rows)

    click.echo(f"Zapisuję dane do {output} w formacie {orient}...")
    selected_df.to_json(output, orient=orient)
    click.echo("Zapisano pomyślnie!")

@cli.command(help="Zapisz dane do pliku Markdown")
@click.option('--input', type=str, required=True,
              help='Ścieżka do pliku CSV')
@click.option('--output', type=str, required=True,
              help='Ścieżka do pliku wyjściowego Markdown')
@click.option('--columns', multiple=True, default=None,
              help='Kolumny do zapisania (domyślnie wszystkie)')
@click.option('--rows', type=int, default=None,
              help='Liczba wierszy do zapisania (domyślnie wszystkie)')
@click.option('--title', type=str, default='Dane',
              help='Tytuł tabeli Markdown (domyślnie "Dane")')
def to_markdown(input, output, columns, rows, title):
    """Wczytaj dane z CSV i zapisz je jako Markdown."""
    click.echo(f"Wczytuje dane z {input}...")
    df = pd.read_csv(input)

    if columns:
        selected_df = df[list(columns)]
    else:
        selected_df = df

    if rows is not None:
        selected_df = selected_df.head(rows)

    click.echo(f"Zapisuję dane do {output}...")

    with open(output, 'w', encoding='utf-8') as f:
        f.write(f"# {title}\n\n")
        f.write(selected_df.to_markdown())

    click.echo("Zapisano pomyślnie!")

if __name__ == '__main__':
    cli()
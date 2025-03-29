import click
import os
from collections import Counter
import re


def count_words(text):
    """Liczy słowa w tekście."""
    words = re.findall(r'\b\w+\b', text.lower())
    return words


@click.group()
def cli():
    """Narzędzie do analizy tekstu."""
    pass


@cli.command(help="Oblicz czas potrzebny na przeczytanie pliku tekstowego")
@click.argument('file_path', type=click.Path(exists=True, readable=True))
def calculate_reading_time(file_path):
    """Oblicza czas potrzebny na przeczytanie pliku tekstowego."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()
            words = count_words(text)
            word_count = len(words)

            reading_time_minutes = word_count / 238

            minutes = int(reading_time_minutes)
            seconds = int((reading_time_minutes - minutes) * 60)

            click.echo(f"Plik: {os.path.basename(file_path)}")
            click.echo(f"Liczba słów: {word_count}")
            click.echo(f"Szacowany czas czytania: {minutes} minut i {seconds} sekund")
    except Exception as e:
        click.echo(f"Błąd: {str(e)}", err=True)


@cli.command(help="Oblicz częstość występowania słów w pliku tekstowym")
@click.argument('file_path', type=click.Path(exists=True, readable=True))
@click.option('--top', type=int, default=10, help="Liczba najczęściej występujących słów do wyświetlenia")
@click.option('--exclude', '-e', multiple=True, default=[], help="Słowa do wykluczenia z analizy")
def calculate_word_frequency(file_path, top, exclude):
    """Oblicza częstość występowania słów w pliku tekstowym."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()
            words = count_words(text)

            filtered_words = [word for word in words if word.lower() not in exclude]

            word_counts = Counter(filtered_words)

            click.echo(f"Plik: {os.path.basename(file_path)}")
            click.echo(f"Top {top} najczęściej występujących słów:")

            for word, count in word_counts.most_common(top):
                click.echo(f"{word}: {count}")
    except Exception as e:
        click.echo(f"Błąd: {str(e)}", err=True)


if __name__ == '__main__':
    cli()


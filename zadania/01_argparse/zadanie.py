import argparse
import pandas as pd

# Użycie:
# poetry run python zadanie.py --url https://raw.githubusercontent.com/mwaskom/seaborn-data/refs/heads/master/titanic.csv
# poetry run python zadanie.py --url https://raw.githubusercontent.com/mwaskom/seaborn-data/refs/heads/master/titanic.csv --columns age alive
# poetry run python zadanie.py --url https://raw.githubusercontent.com/mwaskom/seaborn-data/refs/heads/master/titanic.csv --columns age alive --rows 5
def parse_args():
    parser = argparse.ArgumentParser(description='Wczytaj z url')
    parser.add_argument('--url', type=str, required=True,
                        help='Link do pliku csv')
    parser.add_argument('--columns', nargs='+', default=None,
                        help='Kolumny do wyświetlenia (domyślnie wszystkie)')
    parser.add_argument('--rows', type=int, default=10,
                        help='Liczba wierszy do wyświetlenia (domyślnie 10)')
    return parser.parse_args()

def main():
    args = parse_args()

    print(f"Wczytuje dane z {args.url}...")
    df = pd.read_csv(args.url)

    if args.columns:
        selected_df = df[args.columns]
    else:
        selected_df = df

    print(f"\nWyświetlam pierwsze {min(args.rows, len(selected_df))} wierszy:")
    print(selected_df.head(args.rows))

if __name__ == "__main__":
    main()

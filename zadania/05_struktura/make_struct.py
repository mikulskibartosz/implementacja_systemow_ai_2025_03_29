import os
import argparse

def create_directory(path):
    if not os.path.exists(path):
        os.makedirs(path)
        print(f"Utworzono katalog: {path}")
    else:
        print(f"Katalog już istnieje: {path}")

    keepempty_file = os.path.join(path, ".keepempty")
    if not os.path.exists(keepempty_file):
        with open(keepempty_file, "w") as f:
            f.write("# Ten plik zapewnia, że katalog nie jest pusty i może być śledzony przez git\n")
        print(f"Utworzono plik .keepempty w: {path}")

def create_project_structure(root_dir="."):
    directories = [
        "data/raw",
        "data/processed",
        "data/interim",
        "data/external",
        "models",
        "models/metadata",
        "notebooks",
        "notebooks/utils",
        "src",
        "src/data",
        "src/features",
        "src/models",
        "src/visualization",
        "src/utils",
        "tests",
        "config",
        "docs"
        "reports"
    ]

    for directory in directories:
        full_path = os.path.join(root_dir, directory)
        create_directory(full_path)

    readme_path = os.path.join(root_dir, "README.md")
    if not os.path.exists(readme_path):
        with open(readme_path, "w") as f:
            f.write("# ML Project\n\nOpis projektu znajduje się tutaj.\n")
        print(f"Utworzono README.md w: {root_dir}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Tworzenie struktury projektu ML")
    parser.add_argument("--root-dir", type=str, default=".",
                        help="Katalog główny, w którym zostanie utworzona struktura projektu (domyślnie: bieżący katalog)")
    args = parser.parse_args()

    print(f"Tworzenie struktury projektu w: {args.root_dir}...")
    create_project_structure(args.root_dir)
    print("Struktura projektu została utworzona pomyślnie!")

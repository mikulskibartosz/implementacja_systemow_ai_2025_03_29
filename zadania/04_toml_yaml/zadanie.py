import argparse
import tomllib
import yaml

def deep_merge(first_dict, second_dict):
    merged = first_dict.copy()

    for key, value in second_dict.items():
        if (isinstance(value, dict) and
            key in merged and
            isinstance(merged[key], dict)):
            merged[key] = deep_merge(merged[key], value)
        else:
            merged[key] = value

    return merged

def merge_toml_files(first_file, second_file):
    with open(first_file, 'rb') as f:
        first_config = tomllib.load(f)

    with open(second_file, 'rb') as f:
        second_config = tomllib.load(f)

    merged_config = deep_merge(first_config, second_config)

    return merged_config

def save_as_yaml(config, output_file):
    with open(output_file, 'w') as f:
        yaml.dump(config, f, sort_keys=False)

def main():
    parser = argparse.ArgumentParser(description='Połącz dwa pliki TOML i zapisz jako YAML')
    parser.add_argument('--first-file', dest='first_file', required=True, help='Ścieżka do pierwszego pliku TOML')
    parser.add_argument('--second-file', dest='second_file', required=True, help='Ścieżka do drugiego pliku TOML')
    parser.add_argument('--output-file', dest='output_file', required=True, help='Ścieżka do wyjściowego pliku YAML')

    args = parser.parse_args()

    merged_config = merge_toml_files(args.first_file, args.second_file)

    save_as_yaml(merged_config, args.output_file)

    print(f"Połączona konfiguracja zapisana do {args.output_file}")

if __name__ == "__main__":
    main()

# poetry shell
# python zadanie.py --first-file first.toml --second-file second.toml --output-file merged.yaml
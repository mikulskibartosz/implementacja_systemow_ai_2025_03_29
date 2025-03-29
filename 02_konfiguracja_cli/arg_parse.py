import argparse

def parse_args():
    parser = argparse.ArgumentParser(description='Trenowanie modelu')
    # parser.add_argument("file", type=str,
    #                     help='Ścieżka do danych treningowych')
    parser.add_argument('--data_path', type=str, required=False,
                        help='Ścieżka do danych treningowych')
    parser.add_argument('--model_type', type=str, default='random_forest',
                        choices=['random_forest', 'xgboost', 'neural_network'],
                        help='Typ modelu do treningu')
    parser.add_argument('-v', action='count', default=0,
                        help='Włącza tryb wysyłania logów')
    parser.add_argument("--debug", action="store_true")
    parser.add_argument("--no-cache", action="store_false", dest="cache")
    parser.add_argument("--learning-rate", type=float, default=0.01)
    parser.add_argument("--features", type=str, nargs="+", default=[])
    parser.add_argument("--version", action="version", version="%(prog)s 1.0")
    return parser.parse_args()

args = parse_args()
print("Argumenty:", args)
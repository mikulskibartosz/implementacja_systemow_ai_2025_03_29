import argparse
import joblib
import pandas as pd
import sys
import importlib.resources as pkg_resources
from . import models

def main():
    parser = argparse.ArgumentParser(description='Narzędzie CLI do przewidywania cen domów w Kalifornii')

    # california-housing --med_inc 123 --house_age 5 --avg_rooms 3.5 --avg_bedrms 2 --population 1000 --avg_occup 4 --latitude 37.7749 --longitude -122.4194
    parser.add_argument('--med_inc', type=float, required=True, help='Mediana dochodów w grupie bloków')
    parser.add_argument('--house_age', type=float, required=True, help='Mediana wieku domów w grupie bloków')
    parser.add_argument('--avg_rooms', type=float, required=True, help='Średnia liczba pokoi na gospodarstwo domowe')
    parser.add_argument('--avg_bedrms', type=float, required=True, help='Średnia liczba sypialni na gospodarstwo domowe')
    parser.add_argument('--population', type=float, required=True, help='Populacja grupy bloków')
    parser.add_argument('--avg_occup', type=float, required=True, help='Średnia liczba członków gospodarstwa domowego')
    parser.add_argument('--latitude', type=float, required=True, help='Szerokość geograficzna grupy bloków')
    parser.add_argument('--longitude', type=float, required=True, help='Długość geograficzna grupy bloków')

    args = parser.parse_args()

    features = {
        'MedInc': [args.med_inc],
        'HouseAge': [args.house_age],
        'AveRooms': [args.avg_rooms],
        'AveBedrms': [args.avg_bedrms],
        'Population': [args.population],
        'AveOccup': [args.avg_occup],
        'Latitude': [args.latitude],
        'Longitude': [args.longitude]
    }

    input_df = pd.DataFrame(features)

    try:
        with pkg_resources.path(models, 'model.joblib') as model_path:
            loaded_model = joblib.load(str(model_path))

        prediction = loaded_model.predict(input_df)[0]

        print(f"Przewidywana cena domu: ${prediction:.2f} (w setkach tysięcy)")

    except Exception as e:
        print(f"Błąd podczas przewidywania: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()

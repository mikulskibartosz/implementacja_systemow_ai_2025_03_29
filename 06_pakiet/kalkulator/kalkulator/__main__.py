import argparse

from .kalkulator import predict

def main():
    parser = argparse.ArgumentParser(description="Kalkulator")
    parser.add_argument("--sepal-length", type=float, help="Długość działki")
    parser.add_argument("--sepal-width", type=float, help="Szerokość działki")
    parser.add_argument("--petal-length", type=float, help="Długość płatka")
    parser.add_argument("--petal-width", type=float, help="Szerokość płatka")
    args = parser.parse_args()

    prediction = predict([[args.sepal_length, args.sepal_width, args.petal_length, args.petal_width]])
    print(f"Przewidziana klasa: {prediction}")

if __name__ == "__main__":
    main()
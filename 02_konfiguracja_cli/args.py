import sys

print(f"Nazwa skryptu: {sys.argv[0]}")

if len(sys.argv) > 1:
    print("Argumenty linii poleceń:")
    for i, arg in enumerate(sys.argv[1:], 1):
        print(f"  Argument {i}: {arg}")
from dotenv import load_dotenv
import os

load_dotenv()

print("Aktualnie ustawione zmienne środowiskowe:")
for key in os.environ.keys():
    print(f"- {key}: {os.environ[key]}")

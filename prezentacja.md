## Implementacja Systemów AI

Bartosz Mikulski - Sages

[mikulskibartosz.name](https://mikulskibartosz.name)

[Repozytorium](https://github.com/mikulskibartosz/implementacja_systemow_ai_2025_03_29)
[Prezentacja w PDF](https://mikulskibartosz.github.io/sages_implementacja_systemow_ai/?print-pdf)

---

## Implementacja systemów AI

### Komponenty i Struktura

---

## Oficjalny Plan Zajęć

* Produkcyjna implementacja komponentów systemów AI/ML w oparciu o paradygmat obiektowy
* Budowa produkcyjnych potoków ML'owych
* Zarządzanie strukturą projektu
* Budowa środowiska projektu
* Praca z plikami konfiguracyjnymi

---

## Nasz plan zajęć ;)

1. Jak pisać kod który można użyć ponownie
	1. Zarządzanie zależnościami (pip, poetry, conda, uv)
	2. Konfiguracja (argumenty linii poleceń, zmienne środowiskowe i pliki konfiguracyjne)
	3. Implementacja w oparciu o OOP
	4. Zarządzanie strukturą projektu
	5. Automatyczne testowanie kodu

---
2. Jak przekazać swój kod innym programistom
	1. Publikowanie pakietów Pythonowych
	2. BentoML
	3. Streamlit + REST API - wizualizacja wyników

---

## Zarządzanie zależnościami

---

## Dlaczego zarządzanie zależnościami jest istotne?

* Biblioteki ML często mają **ścisłe zależności** wersji
* Różne projekty mogą potrzebować **różnych wersji** tych samych bibliotek
* Wiele pakietów ML ma **zależności systemowe** (CUDA, MKL, itp.)
* **Odtwarzalność** to fundament nauki i inżynierii
* **Współpraca w zespole** wymaga identycznych środowisk

---

## Kryteria Porównania Narzędzi

* **Izolacja środowiska** - separacja projektów
* **Zarządzanie wersjami Pythona** - wsparcie dla wielu wersji
* **Rozwiązywanie konfliktów** - radzenie sobie z niekompatybilnościami
* **Odtwarzalność** - gwarancja identycznych środowisk
* **Szybkość** - czas instalacji pakietów
* **Obsługa pakietów niepythonowych** - C/C++, CUDA, itp.

---

## Porównanie Narzędzi

| Kryterium | pip+venv | conda | poetry | uv |
|-----------|----------|-------|--------|------|
| Izolacja | ✓ (venv) | ✓✓✓ | ✓✓ | ✓ (venv) |
| Wersje Pythona | ✗ | ✓✓✓ | ✓ | ✓ |
| Rozwiązywanie konfliktów | ✗ | ✓✓ | ✓✓✓ | ✓✓ |
| Odtwarzalność | ✓ | ✓✓ | ✓✓✓ | ✓✓ |
| Szybkość | ✓✓ | ✗ | ✓ | ✓✓✓ |
| Pakiety niepythonowe | ✗ | ✓✓✓ | ✗ | ✗ |

---

## pip + venv

**Podstawowe narzędzie ekosystemu Python**

* Standardowy menedżer pakietów Python
* Środowiska tworzone przez moduł **venv** (Python 3.3+)
* Definicja zależności w pliku **requirements.txt**
* Prosty i powszechnie używany
* Ograniczone rozwiązywanie konfliktów zależności

---

## pip + venv: Podstawowe Komendy

**Tworzenie środowiska**
```bash
python -m venv env
source env/bin/activate  # Linux/Mac
env\Scripts\activate     # Windows
```

**Instalacja pakietów**
```bash
pip install numpy pandas scikit-learn
pip install -r requirements.txt
```

**Eksport zależności**
```bash
pip freeze > requirements.txt
```

---

## pip + venv: Plik requirements.txt

```
# requirements.txt
numpy==1.24.3
pandas==2.0.1
scikit-learn==1.2.2
matplotlib>=3.7.1
```

* Dokładne wersje `==` zapewniają odtwarzalność
* Wersje minimalne `>=` dają elastyczność (ale mniejszą odtwarzalność)
* Można dodawać komentarze z `#`
* Brak hierarchii zależności

---

## pip: Instalacja w trybie edycji

**Instalacja własnego pakietu w trybie dev**

```bash
pip install -e .
```

* Pakiet zostaje zainstalowany jako symlink do kodu źródłowego
* Zmiany w kodzie są natychmiast widoczne bez reinstalacji
* Niezbędne podczas pracy nad własnym pakietem
* Wymaga pliku `setup.py` lub `pyproject.toml`

---

## conda

**Kompleksowy menedżer środowisk i pakietów**

* Zarządza środowiskami, pakietami **i wersjami Pythona**
* Obsługuje pakiety Pythona i **zależności binarne** (C, C++, R)
* Świetne wsparcie dla pakietów naukowych i ML
* Rozwiązuje konflikty zależności
* Kanały dystrybucji (conda-forge, bioconda, itp.)
* Wolniejsze od pip

---

## Anaconda vs Miniconda

**Anaconda**
* Pełna dystrybucja (3GB+)
* Zawiera 1500+ pakietów naukowych
* Anaconda Navigator (GUI)
* Dobra dla początkujących

**Miniconda**
* Minimalna instalacja (400MB)
* Tylko Python, conda i podstawowe pakiety
* Trzeba ręcznie instalować potrzebne pakiety
* Lepsza dla doświadczonych użytkowników i CI/CD

---

## conda: Podstawowe Komendy

**Tworzenie środowiska**
```bash
conda create -n ml-project python=3.10
conda activate ml-project
```

**Instalacja pakietów**
```bash
conda install numpy pandas scikit-learn
conda install -c conda-forge lightgbm
```

**Eksport/import środowiska**
```bash
conda env export > environment.yml
conda env create -f environment.yml
```

---

## conda: Plik environment.yml

```yaml
name: ml-project
channels:
  - conda-forge
  - defaults
dependencies:
  - python=3.10
  - numpy=1.24.3
  - pandas=2.0.1
  - scikit-learn=1.2.2
  - pip:
    - some-package-not-in-conda==1.0.0
```

* Definicja nazwy środowiska
* Lista kanałów dystrybucji
* Zależności z określonymi wersjami
* Możliwość dodania pakietów z pip

---

## poetry

**Nowoczesne narzędzie do zarządzania zależnościami**

* Menedżer pakietów i zależności inspirowany npm/cargo
* Deklaratywna konfiguracja w **pyproject.toml**
* **Plik lock** zapewniający odtwarzalność
* Inteligentne rozwiązywanie konfliktów
* Grupy zależności (dev, test, docs)
* Wsparcie dla publikowania pakietów
* Wbudowana obsługa środowisk wirtualnych

---

## poetry: Podstawowe Komendy

**Utworzenie projektu**
```bash
poetry new ml-project
cd ml-project
```

**Instalacja pakietów**
```bash
poetry add numpy pandas scikit-learn
poetry add --group dev pytest black
```

**Aktywacja środowiska i uruchamianie**
```bash
poetry shell
poetry run python script.py
```

**Instalacja z pliku lock**
```bash
poetry install --no-dev  # bez zależności deweloperskich
```

---

## poetry: Plik pyproject.toml

```toml
[tool.poetry]
name = "ml-project"
version = "0.1.0"
description = "Projekt uczenia maszynowego"
authors = ["Twoje Imię <email@example.com>"]

[tool.poetry.dependencies]
python = ">=3.9,<3.11"
numpy = "^1.24.0"
pandas = "^2.0.0"
scikit-learn = "^1.2.0"

[tool.poetry.group.dev.dependencies]
pytest = "^7.3.1"
black = "^23.3.0"

[build-system]
requires = ["poetry-core>=1.0.0"]
build-backend = "poetry.core.masonry.api"
```

---

## uv

**Szybkie narzędzie do instalacji pakietów**

* **Znacznie szybsze** od innych rozwiązań
* Kompatybilne z istniejącymi formatami (requirements.txt, pyproject.toml)
* Instalacja w trybie edycji dla rozwoju
* Wsparcie dla plików lock
* W pełni kompatybilne z pip
* Rosnąca popularność w społeczności Python

---

## uv: Podstawowe Komendy

**Instalacja uv**
```bash
pip install uv
```

**Tworzenie środowiska i instalacja pakietów**
```bash
uv venv
source .venv/bin/activate  # Linux/Mac
.venv\Scripts\activate     # Windows

uv pip install numpy pandas scikit-learn
uv pip install -r requirements.txt
```

---

## uv: Ustawienie wersji Pythona

**Tworzenie środowiska z konkretną wersją Pythona**
```bash
uv venv --python=python3.9
```

**Używanie uv z pyenv**
```bash
pyenv install 3.9.10
pyenv local 3.9.10
uv venv
```

* UV używa Pythona dostępnego w systemie
* Dla zarządzania wersjami Pythona warto łączyć uv z pyenv

---

## Porównanie Wydajności

**Czas instalacji typowych pakietów ML**

| Narzędzie | Czas instalacji |
|-----------|-----------------|
| pip       | ⭐⭐          |
| conda     | ⭐             |
| poetry    | ⭐⭐          |
| uv        | ⭐⭐⭐⭐      |

* uv może być nawet **10-100x szybsze** niż pip w niektórych scenariuszach
* conda jest zazwyczaj najwolniejsza ze względu na złożone rozwiązywanie zależności
* Dla CI/CD i dużych zespołów, różnice w wydajności są znaczące

---

## Pakiety z komponentami C/C++

**Typowe problemy**
* Konieczność posiadania kompilatora (gcc, clang, MSVC)
* Zależności systemowe (OpenBLAS, CUDA)
* Różnice między platformami

**Rozwiązania**
* **conda**: Dostarcza gotowe pliki binarne `conda install numpy`
* **pip wheels**: "Precompiled binaries" `pip install numpy`
* **System**: Instalacja zależności systemowych
  * Ubuntu: `apt install build-essential python3-dev`
  * macOS: `xcode-select --install`
  * Windows: Visual C++ Build Tools

---

## Kiedy używać poszczególnych narzędzi?

**pip + venv**
* Proste projekty z niewielką liczbą zależności
* Gdy priorytetem jest prostota i standardowość

**conda**
* Projekty wykorzystujące GPU i pakiety naukowe
* Gdy potrzebujesz niestandardowych wersji Pythona
* Gdy potrzebujesz pakietów niepythonowych (C/C++, R)

---

## Kiedy używać poszczególnych narzędzi? (cd.)

**poetry**
* Gdy tworzysz pakiet do dystrybucji
* Gdy zależy Ci na szczegółowej kontroli zależności
* Duże projekty zespołowe z wieloma zależnościami

**uv**
* Gdy szybkość jest priorytetem (CI/CD)
* Jako zamiennik pip w istniejących projektach
* Przy instalacji dużej liczby pakietów

---

## Najlepsze Praktyki

* Używaj **dokładnych wersji** dla krytycznych zależności
* Zawsze korzystaj z **plików lock** gdy to możliwe
* Umieszczaj definicje środowiska w **repozytorium**
* Testuj odtwarzanie środowiska na **czystej maszynie**
* Dokumentuj **nietypowe zależności** systemowe
* Rozważ **konteneryzację** (Docker) dla pełnej izolacji
* Wybieraj narzędzia adekwatne do **złożoności projektu**

---

## Łączenie narzędzi

**Popularne kombinacje**

* **conda + pip**
  ```yaml
  # environment.yml
  dependencies:
    - python=3.10
    - numpy
    - pip:
      - tensorflow
  ```

* **poetry + pyenv** - dla zarządzania Pythonem
* **uv + pip-requirements** - przyspieszone instalacje

---

## Podsumowanie

* **pip+venv**: standardowe, proste, wbudowane w Python
* **conda**: potężne, obsługuje pakiety binarne, popularne w DS/ML
* **poetry**: nowoczesne, odtwarzalne, dobre do publikacji pakietów
* **uv**: szybkie, kompatybilne z istniejącymi formatami

---

## Repozytoria pakietów

* https://pypi.org/
* https://anaconda.org/

---

## Ćwiczenia

pip, poetry, conda, uv

---

## Konfiguracja w Projektach ML

---

## Dlaczego zarządzanie konfiguracją jest ważne?

* **Odtwarzalność** eksperymentów ML
* **Elastyczność** - łatwa zmiana parametrów bez modyfikacji kodu
* **Automatyzacja** - zautomatyzowane przebiegi i eksperymenty
* **Kontrola wersji** - śledzenie zmian w konfiguracji
* **Współpraca** w zespole
* **CI/CD** - integracja z pipelinami

---

## Metody konfiguracji

1. **Argumenty linii poleceń**
   * Najprostsze i najbardziej bezpośrednie
   * Idealne dla jednorazowych uruchomień i szybkiego prototypowania

2. **Zmienne środowiskowe**
   * Dobre dla CI/CD i konteneryzacji
   * Idealne dla danych wrażliwych (hasła, klucze API)

3. **Pliki konfiguracyjne**
   * Najlepsze dla złożonych konfiguracji
   * Wspierają hierarchiczne struktury danych

---

## Argumenty linii poleceń

**Zalety:**
* Szybkie i proste dla prostych skryptów
* Natychmiastowa widoczność użytych parametrów
* Dobra dokumentacja (--help)

**Wady:**
* Nieporęczne dla dużej liczby parametrów
* Ograniczone struktury danych
* Trudne do umieszczenia w kontroli wersji

**Biblioteki:**
* sys.argv
* argparse (standardowa biblioteka)
* click, fire (zewnętrzne)

---

## Przykład: sys.argv

```bash
poetry run python args/sysargv.py to jest test
```

---

## Kod sys.argv

```python
import sys

print(f"Nazwa skryptu: {sys.argv[0]}")

if len(sys.argv) > 1:
    print("Argumenty linii poleceń:")
    for i, arg in enumerate(sys.argv[1:], 1):
        print(f"  Argument {i}: {arg}")
```

---

## sys.argv

* Wady:
  * Nie ma walidacji typów
  * Nie ma obsługi domyślnych wartości
  * Wszystko jest tekstem
  * Kolejność argumentów jest ważna

* Zalety:
  * ???

---

## argparse

```bash
poetry run python args/arg_parse.py --help
poetry run python args/arg_parse.py --data_path data/train.csv --model_type random_forest --n_estimators 100
```

---

## argparse

```python
import argparse

def parse_args():
    parser = argparse.ArgumentParser(description='Trenowanie modelu')
    parser.add_argument('--data_path', type=str, required=True,
                        help='Ścieżka do danych treningowych')
    parser.add_argument('--model_type', type=str, default='random_forest',
                        choices=['random_forest', 'xgboost', 'neural_network'],
                        help='Typ modelu do treningu')
    ...
    return parser.parse_args()

args = parse_args()
print(f"Trenuję model {args.model_type} na danych z {args.data_path}")
```

---

## ZADANIE 1 (10 minut)

Użyj argparse w celu implementacji skryptu, który:
1. Wczyta csv z podanego URL (argument obowiązkowy)
2. Wyświetli wybrane przez użytkownika kolumny (argumenty opcjonalne, domyślnie wszystkie)
3. Wyświetli wybraną liczbę wierszy (argument opcjonalny, domyślnie 10)

[Przykładowy url](https://raw.githubusercontent.com/mwaskom/seaborn-data/refs/heads/master/titanic.csv)

---

## click

Alternatywa dla argparse pozwalająca na tworzenie złożonych interfejsów wiersza poleceń.

https://click.palletsprojects.com

---

## Click - jedna funkcja

```python
@click.command(help="Trenowanie modelu")
@click.option('--data_path', type=str, required=True,
              help='Ścieżka do danych treningowych')
@click.option('--model_type', type=click.Choice(['random_forest', 'xgboost', 'neural_network']),
              default='random_forest', help='Typ modelu do treningu')
@click.option('-v', 'verbose', count=True,
              help='Włącza szczegółowe logowanie')
@click.option('--debug/--no-debug', default=False,
              help='Włącza tryb debugowania')
@click.option('--cache/--no-cache', default=True,
              help='Włącza lub wyłącza cache')
@click.option('--features', multiple=True, default=[],
              help='Lista cech do użycia w modelu')
...
@click.version_option(version='1.0')
def train(data_path, model_type, verbose, debug, cache, learning_rate, max_depth, features, n_estimators):
```

---

## Click - wiele funkcji

```python
@click.group()
def cli():
    """Aplikacja do konwertowania danych CSV."""
    pass

@cli.command(help="Zapisz dane do pliku JSON")
...

@cli.command(help="Zapisz dane do pliku XML")
```

[Wiele funkcji w różnych plikach](https://click.palletsprojects.com/en/stable/quickstart/#registering-commands-later)

---

## Click

[Typy danych](https://click.palletsprojects.com/en/stable/parameters/#parameter-types):

```python
@click.argument('file_path', type=click.Path(exists=True, readable=True))
```

Click Echo (można też używać print):
```python
click.echo('Hello, World!')
click.echo('Exception', err=True)
```

---

## ZADANIE 2 (15 minut)

Użyj Click w celu implementacji skryptu, który:
1. Zaimplementuje dwie funkcje:
    1. `calculate_reading_time` - oblicza czas potrzebny na przeczytanie tekstu

		Średnia dla osoby dorosłej czytającej tekst w j. angielskim wynosi [238 słów na minutę](https://scholarwithin.com/average-reading-speed#adult-average-reading-speed)
    2. `calculate_word_frequency` - oblicza częstość występowania słów w tekście
2. Obie przyjmują ścieżkę do pliku tekstowego jako obowiązkowy argument
3. Druga funkcja przyjmuje argument określający liczbę najczęściej występujących słów do wyświetlenia (domyślnie 10)
4. Oraz listę słów do wykluczenia z analizy (argument opcjonalny, domyślnie pusta lista)

---

## Zmienne środowiskowe

**Zalety:**
* Idealne dla danych wrażliwych (hasła, tokeny API)
* Dobre dla konteneryzacji (Docker, Kubernetes)
* Wspierane we wszystkich systemach i środowiskach CI/CD

**Wady:**
* Trudniejsze debugowanie (mniejsza widoczność)
* Ograniczona struktura danych (tylko proste wartości)
* Problemy z typowaniem (wszystko jest stringiem)

**Biblioteki:**
* os.environ (standardowa biblioteka)
* python-dotenv, environs

---

## Przykład: os.environ

```python
import os

# Odczyt zmiennych środowiskowych z opcjonalnymi wartościami domyślnymi
DATABASE_URL = os.environ.get('DATABASE_URL', 'sqlite:///default.db')
API_KEY = os.environ.get('API_KEY')  # Brak wartości domyślnej
DEBUG = os.environ.get('DEBUG', 'False').lower() == 'true'  # String -> bool
MODEL_VERSION = int(os.environ.get('MODEL_VERSION', '1'))  # String -> int

print(f"Połączenie z bazą: {DATABASE_URL}")
print(f"Debug mode: {DEBUG}")

# Sprawdzenie czy kluczowe zmienne są ustawione
if API_KEY is None:
    raise ValueError("Brak wymaganej zmiennej środowiskowej API_KEY")
```
---

## Przykład: os.environ - użycie

```bash
export API_KEY=1234567890

API_KEY=1234567890 poetry run python env/env_var.py
```

---

## dotenv

Plik `.env`:
```
DATABASE_URL=postgresql://user:password@localhost/ml_db
API_KEY=sk_test_abcdefghijklmnopqrstuvwxyz
DEBUG=true
```

---

## dotenv - użycie

```python
from dotenv import load_dotenv
import os

# Załadowanie zmiennych z pliku .env
load_dotenv()

# Odczyt zmiennych środowiskowych z użyciem os.environ
DATABASE_URL = os.environ.get('DATABASE_URL', 'sqlite:///default.db')
API_KEY = os.environ.get('API_KEY')
DEBUG = os.environ.get('DEBUG', 'False').lower() == 'true'

...
```

---

## Dotenv - nadpisywanie zmiennych

```bash
API_KEY=1234567890 poetry run python env/env_var.py
```

---

## ZADANIE 3 (10 minut)

Użyj python-dotenv w celu implementacji skryptu, który:
1. Wczyta zmienne środowiskowe z pliku `.env`
2. Wyświetli wszystkie aktualnie ustawione zmienne środowiskowe (`os.environ.keys()`)

---

## Pliki konfiguracyjne

**Zalety:**
* Obsługa złożonych, hierarchicznych struktur danych
* Łatwe umieszczenie w kontroli wersji
* Dobra czytelność i możliwość komentowania
* Łatwa wymiana między środowiskami

**Wady:**
* Wymaga dodatkowego kodu do parsowania
* Więcej możliwości błędów i problemów z typami
* Trudniejsze zarządzanie danymi wrażliwymi

**Formaty:**
* YAML, TOML, ...

---

## Pydantic

https://docs.pydantic.dev/latest/

---

## Pydantic - Walidacja danych

* Biblioteka do walidacji i serializacji danych
* Automatyczna konwersja typów
* Integracja z typami z modułu `typing`
* Obsługa wartości domyślnych
* Walidacja danych wejściowych

---

```python
from pydantic import BaseModel, Field
from typing import Optional

class ModelConfig(BaseModel):
    type: str
    n_estimators: int = 100
    max_depth: Optional[int] = None
    random_state: int = 42
```

---

## TOML

https://toml.io/en/

---

```toml
title = "TOML Example"

[owner]
name = "Tom Preston-Werner"
dob = 1979-05-27T07:32:00-08:00

[database]
enabled = true
ports = [ 8000, 8001, 8002 ]
data = [ ["delta", "phi"], [3.14] ]
temp_targets = { cpu = 79.5, case = 72.0 }

[servers]

[servers.alpha]
ip = "10.0.0.1"
role = "frontend"

[servers.beta]
ip = "10.0.0.2"
role = "backend"
```

---

## Wczytywanie TOML

```python
import tomllib

config = tomllib.load(file)

```

---

## Zapisywanie YAML i TOML

```python
yaml.dump(config_dict, f)
```

https://tomlkit.readthedocs.io/en/latest/

---

## ZADANIE 4 (15 minut)

Dane są dwa pliki toml.

1. Napisz skrypt, który przyjmie ścieżki do obu plików jako argumenty.
2. Połączy oba pliki w jeden, nadpisując wartości z pliku pierwszego wartościami z pliku drugiego.
3. Zapisze wynik do pliku yaml. Ścieżka do pliku yaml również jest argumentem.

---

## Bezpieczeństwo konfiguracji

**Wrażliwe dane w konfiguracji:**
* Hasła do baz danych
* Klucze API
* Tokeny dostępu
* Certyfikaty

**Dobre praktyki:**
* **Nigdy** nie przechowuj sekretów w repozytorium
* Używaj zmiennych środowiskowych dla danych wrażliwych
* Rozważ dedykowane narzędzia (Vault, AWS Secrets Manager)
* Używaj plików `.env` dla lokalnego rozwoju (dodaj do `.gitignore`)
* Rozważ szyfrowanie plików konfiguracyjnych

---

## Najlepsze praktyki

* **Zasada pojedynczej odpowiedzialności** - oddziel konfigurację od logiki
* **Waliduj dane wejściowe** - nie zakładaj, że konfiguracja jest poprawna
* **Używaj wartości domyślnych** - aplikacja powinna działać z minimalnymi ustawieniami
* **Dokumentuj konfigurację** - komentarze, przykłady, schematy
* **Pliki przykładowe** - dodaj `config.example.yaml` do repo
* **Unikaj zbyt dużej złożoności** - konfiguracja powinna być prosta
* **Testuj z różnymi konfiguracjami** - uwzględnij testy dla różnych ustawień

---

## Paradygmat obiektowy w ML

---

### Problemy notebooków

* kod jednorazowego użytku (użycie wielokrotne przez kopiowanie)
* trudność w testowaniu
* komórki notebooka można uruchamiać w dowolnej kolejności
* zapisywanie notebooków w repozytorium
	* ogromne pliki,
	* diff nie zawiera tylko kodu
* praca wielu osób w tym samym pliku
* wdrożenie notebooka (możliwe, ale nie zalecane)

---

## Techniczne sposoby dzielenia kodu

### OOP
* moduły
* klasy
* metody i pola

---

### Funkcyjny
* funkcje (def, lambda)
* struktury danych (namedtuple, dict, list, tuple, dataclass)
* funkcje wyższych rzędów (map, filter, reduce)

---

## Kryteria podziału kodu

### SOLID
* **S**ingle Responsibility Principle - jedna klasa, jedna odpowiedzialność
* **O**pen-Closed Principle - otwarte na rozszerzanie, zamknięte na modyfikacje
* **L**iskov Substitution Principle - obiekty klas pochodnych mogą zastępować obiekty klas bazowych

---

* **I**nterface Segregation Principle - wiele dedykowanych interfejsów zamiast jednego ogólnego
* **D**ependency Inversion Principle - zależności od abstrakcji, nie konkretnych implementacji

---

### CUPID Properties

Dan North - [CUPID—for joyful coding](https://dannorth.net/cupid-for-joyful-coding/)

---

* **C**omposable - komponowalne, można je łączyć w większe systemy
* **U**nix Philosophy - zgodne z filozofią Uniksa, robią jedną rzecz dobrze
* **P**redictable - przewidywalne, zachowują się zgodnie z oczekiwaniami
* **I**diomatic - zgodne z konwencjami języka
* **D**omain-based - oparte na domenie, odzwierciedlają język biznesowy

---

### Unix Philosophy

[Unix Philosophy](https://cscie2x.dce.harvard.edu/hw/ch01s06.html)

> This is the Unix philosophy: Write programs that do one thing and do it well. Write programs to work together. Write programs to handle text streams, because that is a universal interface.

---

### Unix Philosophy w działaniu

```bash
cat README.md | grep "https" | sort | uniq
```

---

### SOLID w kontekście ML

* **S**ingle Responsibility Principle
  * Działa dobrze na poziomie funkcji i klas
  * Niekoniecznie na poziomie całych potoków ML

* **O**pen-Closed Principle
  * W ML często lepiej po prostu zmienić kod transformacji
  * Nadmierna abstrakcja ogranicza czytelność kodu

---

* **L**iskov Substitution Principle
  * Bardzo przydatne! Możemy zamieniać komponenty nie wpływając na konsumentów
  * Przykład: wymiana implementacji feature engineeringu bez zmian w kolejnych krokach

---

* **I**nterface Segregation Principle
  * Często niepraktyczne w ML - prowadzi do duplikacji obliczeń
  * Lepiej policzyć wszystkie wyniki raz i wybrać potrzebne

---

* **D**ependency Inversion Principle
  * Zbyt skomplikowane dla większości potoków ML
  * Overengineering w kontekście transformacji danych

---

### CUPID w kontekście ML

* **C**omposable - komponowalne
  * Dane wyjściowe jednego kroku są wejściowymi dla następnego
  * Naturalna cecha potoków danych

* **U**nix Philosophy - filozofia Uniksa
  * Każdy komponent robi jedną rzecz dobrze
  * Wyjście jednego programu staje się wejściem dla innego

---

* **P**redictable - przewidywalne
  * Deterministyczne, testowalne zachowanie
  * Automatyczne testy jako kluczowy element

* **I**diomatic - idiomatyczne
  * Zgodne z konwencjami i najlepszymi praktykami Pythona
  * Wykorzystanie bibliotek i narzędzi ekosystemu Python
  * Nie próbujemy zamieniać Pythona w Javę... lub Haskella

---

* **D**omain-based - oparte na domenie
  * Używanie terminologii biznesowej w kodzie
  * Logiki domenowej w dedykowanych funkcjach i strukturach danych
  * Wewnątrz kodu ML: proste typy danych (string, float, int)
  * Publiczne API: typy domenowe (klasy, enum)

---

## Filozofia Unix w ML

"Make each program do one thing well. (...) Expect the output of every program to become the input to another."

* Pipeline ML jako łańcuch małych, specjalizowanych komponentów
* Każdy komponent ma jasno zdefiniowane wejście i wyjście
* Komponenty można łączyć w różne konfiguracje

---

## Unix Philosophy

<section style="text-align: left;">
  <blockquote>
    Rule of Modularity: Write simple parts connected by clean interfaces. <br>
    Rule of Clarity: Clarity is better than cleverness. <br>
    ... <br>
    Rule of Repair: When you must fail, fail noisily and as soon as possible. <br>
    ... <br>
    <strong>Rule of Diversity: Distrust all claims for "one true way".</strong>
  </blockquote>
</section>

---

## Zarządzanie strukturą projektu

---

## Dlaczego struktura projektu jest ważna?

* Ułatwia **współpracę** w zespole
* Zapewnia **powtarzalność** eksperymentów
* Pozwala **śledzić zmiany** w czasie
* Oddziela **kod od danych**
* Umożliwia **testowanie** komponentów
* Usprawnia **wdrażanie** do produkcji

---

## Przykładowa Struktura Projektu ML

```
projekt_ml/
├── data/               # Wszystkie dane projektu
│   ├── raw/            # Niezmienione, oryginalne dane
│   ├── processed/      # Dane po wstępnym przetworzeniu
│   ├── interim/        # Dane pośrednie
│   └── external/       # Dane z zewnętrznych źródeł
├── models/             # Wytrenowane modele i artefakty
├── notebooks/          # Jupyter notebooks (eksploracja, prototypy)
├── src/                # Kod źródłowy aplikacji
├── tests/              # Testy jednostkowe i integracyjne
├── config/             # Pliki konfiguracyjne
├── docs/               # Dokumentacja
├── reports/            # Wyniki eksperymentów
└── README.md           # Opis projektu
```

---

## Zarządzanie Danymi

* **Raw data** (surowe dane)
  * Nigdy nie modyfikuj!
  * Zapisuj metadane (skąd, kiedy, wersja)

* **Processed data** (przetworzone dane)
  * Oczyszczone, przekształcone
  * Gotowe do modelowania
  * Zachowuj ścieżkę przetwarzania

---

* **Interim data** (dane pośrednie)
  * Przydatne dla długich pipeline'ów
  * Checkpointy przetwarzania
  * Łatwiejsze debugowanie

* **External data** (dane zewnętrzne)
  * Dane referencyjne
  * Dane do wzbogacania głównego zbioru
  * Benchmarki

---

## Organizacja kodu

```
src/
├── init.py
├── data/                 # Skrypty do przetwarzania danych
│   ├── init.py
│   ├── make_dataset.py
│   └── preprocess.py
├── features/             # Feature engineering
│   ├── init.py
│   └── build_features.py
├── models/               # Definicje modeli, trening
│   ├── init.py
│   ├── train_model.py
│   └── predict_model.py
├── visualization/        # Wizualizacje
└── utils/                # Narzędzia pomocnicze
```

---

## Modularyzacja Projektu

* **Moduły wg funkcjonalności**
  * Data processing
  * Feature engineering
  * Model training
  * Evaluation

---

## Modularyzacja Projektu

* **Moduły wg przepływu danych**
  * Preprocessing
  * Training
  * Inference
  * Monitoring

---

## Notebooks vs. Kod Źródłowy

**Notebooks (`/notebooks`)**
* Eksploracja danych
* Prototypowanie
* Wizualizacja
* Prezentacja wyników

---

## Notebooks vs. Kod Źródłowy

**Kod źródłowy (`/src`)**
* Przetwarzanie danych
* Implementacja modeli
* Produkcyjna logika biznesowa
* Komponenty wielokrotnego użytku

---

## Organizacja Notebooków

```
notebooks/
├── 01-bm-wstepna-eksploracja-danych.ipynb
├── 02-bm-feature-engineering.ipynb
├── 03-bm-model-baseline.ipynb
├── 04-bm-model-tuning.ipynb
└── utils/
└── helpers.py
```

---

## Organizacja Notebooków

* Prefiks numeryczny dla kolejności
* Inicjały autora
* Krótki opis zawartości
* Wspólne funkcje pomocnicze w osobnym module

---

## Modele

```
models/
├── 2025-03-29-rf-default-params.pkl
├── 2025-03-30-rf-tuned-params.pkl
└── metadata/
    ├── 2025-03-29-rf-default-params.yaml
    └── 2025-03-30-rf-tuned-params.yaml
```

---

## Modele

* Konwencja nazewnictwa: data-model-info
* Metadane zawierające:
  * Parametry modelu
  * Metryki wydajności
  * Ścieżka do danych treningowych
  * Hash danych treningowych

---

## Konfiguracja Projektu

**Opcje konfiguracji**
* Pliki YAML lub TOML w `/config`
* Zmienne środowiskowe (przez `.env`)
* Config jako kod w Pythonie

---

### Co konfigurować?

* Ścieżki do danych
* Parametry modeli
* Flagi feature toggles
* Ustawienia eksperymentów

---

## Najczęstsze błędy

<section style="text-align: left;">
❌ Wszystko w jednym folderze<br>
❌ Mieszanie kodu, danych i modeli<br>
❌ Brak konwencji nazewnictwa<br>
❌ Modyfikowanie oryginalnych danych<br>
❌ Brak śledzenia eksperymentów<br>
❌ "Notebook hell" - cały kod w notebookach<br>
</section>

---

## Zadanie 5 A (15 minut)

Identyfikacja problemów z kodem w notebooku

---

## Zadanie 5 B (25 minut)

Implementacja kodu w oparciu o dobre praktyki

---

## Automatyczne testowanie w Pythonie

---

## Agenda

* **Przypomnienie pytest**
* **Wprowadzenie do Behave i BDD**
* **Testowanie właściwościowe**
* **Porównanie podejść**
* **Ćwiczenia praktyczne**

---

## Dlaczego warto znać różne metody testowania?

* **Różne problemy, różne narzędzia**
* **Lepsza komunikacja** z nietechnicznymi członkami zespołu
* **Wykrywanie różnych typów błędów**
* **Kompletna strategia testowania**
* **Dopasowanie do specyfiki projektu**

---

## Przypomnienie pytest

* **Prosta składnia** oparta o funkcje i asercje
* **Bogate komunikaty błędów**
* **Fixtures** do współdzielenia stanu
* **Parametryzacja** testów
* **Markery** do kategoryzacji


---

## Konwencja nazewnictwa testów

* katalog `tests`
* plik `test_<nazwa_testu>.py`
* funkcja `test_<nazwa_testu>()`

---

## Podstawowy test pytest

```python
# test_calculator.py
def add(a, b):
    return a + b

def test_add():
    assert add(1, 2) == 3
    assert add(-1, 1) == 0, "Komunikat błędu"
    assert add(-1, -1) == -2
```

Uruchomienie: `pytest test_calculator.py -v`

---

## Fixtures w pytest

```python
@pytest.fixture
def empty_db():
    """Fixture dostarczający czystą bazę użytkowników."""
    return UserDatabase()

def test_get_users_by_role(empty_users):
	...

---

## Parametryzacja testów

```python
@pytest.mark.parametrize("input_text,expected", [
    ("hello world", "Hello World"),
    ("python test", "Python Test"),
    ("a b c", "A B C"),
    ("", ""),
    ("already Capitalized", "Already Capitalized")
])
def test_capitalize_words(input_text, expected):
    result = capitalize_words(input_text)
    assert result == expected
```

---

## BDD i Behave

**Behavior-Driven Development (BDD):**
* Specyfikacje jako wykonywalne testy
* Język zrozumiały dla wszystkich interesariuszy
* Skupienie na zachowaniu, a nie implementacji

**Behave:**
* Framework BDD dla Pythona
* Używa języka Gherkin (Given-When-Then)

---

## Struktura projektu Behave

```
features/
  ├── steps/
  │     ├── __init__.py
  │     └── calculator_steps.py
  ├── environment.py
  └── calculator.feature
```

* **feature** - Pliki z opisem funkcjonalności
* **steps** - Implementacja kroków
* **environment.py** - Konfiguracja testów

---

## Przykład scenariusza Behave

```gherkin
# features/calculator.feature
Feature: Calculator functionality
  As a user
  I want to perform basic arithmetic operations
  So that I can do quick calculations

  Scenario: Addition of two numbers
    Given I have a calculator
    When I add 5 and 7
    Then the result should be 12

  Scenario: Subtraction of two numbers
    Given I have a calculator
    When I subtract 8 from 15
    Then the result should be 7
```

---

```python
# features/steps/calculator_steps.py
from behave import given, when, then

class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

@given('I have a calculator')
def step_impl(context):
    context.calculator = Calculator()
```

---

```python
@when('I add {a:d} and {b:d}')
def step_impl(context, a, b):
    context.result = context.calculator.add(a, b)

@when('I subtract {b:d} from {a:d}')
def step_impl(context, a, b):
    context.result = context.calculator.subtract(a, b)

@then('the result should be {result:d}')
def step_impl(context, result):
    assert context.result == result
```

---

## Działanie

* każdy krok ma `context`
* `context` służy do współdzielenia informacji między krokami (w ramach jednego scenariusza)
* np. w kroku `given` tworzymy obiekt, który będzie używany w kolejnych krokach
* w kroku `when` zapisujemy rezultaty w `context`
* w kroku `then` sprawdzamy wartości w `context`

---

## Parametryzacja

```gherkin
Scenario Outline: Addition with multiple examples
Given I have a calculator
When I add <first> and <second>
Then the result should be <expected>

Examples:
  | first | second | expected |
  | 1     | 1      | 2        |
  | -1    | 1      | 0        |
  | -1    | -1     | -2       |
  | 0     | 0      | 0        |
  | 10    | 20     | 30       |

```

---

## Tabele danych

```gherkin
Scenario: Addition with data table
Given I have a calculator
When I perform the following additions:
  | first | second | expected |
  | 1     | 2      | 3        |
  | 5     | 5      | 10       |
  | -3    | 3      | 0        |
  | 10    | -5     | 5        |
  | 100   | 200    | 300      |
Then all results should be correct
```

---

## Tabele danych - Python

```python
@when('I perform the following additions')
def step_impl(context):
    for row in context.table:
        a = int(row['first'])
        b = int(row['second'])
        expected = int(row['expected'])
        ...
```

---

## Testowanie właściwościowe

**Koncepcja:**
* Testowanie **ogólnych właściwości** zamiast konkretnych przypadków
* Automatyczne **generowanie danych testowych**
* Znajdowanie **minimalnych kontrprzykładów**
* Odkrywanie **nieoczywistych błędów**

**Główne narzędzie:**
* **Hypothesis** - biblioteka property-based testing dla Pythona

---

## Przykład testowania właściwościowego

```python
from hypothesis import given, strategies as st

def reverse_list(lst):
    return lst[::-1]

@given(st.lists(st.integers()))
def test_reverse_twice_is_identity(lst):
    """Test czy podwójne odwrócenie listy = tożsamość."""
    assert reverse_list(reverse_list(lst)) == lst
```

---

## Generatory danych w Hypothesis

* **st.integers()** - liczby całkowite
* **st.floats()** - liczby zmiennoprzecinkowe
* **st.lists()** - listy
* **st.tuples()** - krotki
* **st.dictionaries()** - słowniki
* **st.text()** - tekst

---

## Porównanie podejść do testowania

| Kryterium | pytest | Behave (BDD) | Testowanie właściwościowe |
|-----------|--------|--------------|---------------------------|
| **Cel testowania** | Jednostki | Zachowanie | Właściwości |
| **Czytelność dla nietechnicznego zespołu** | Średnia | Wysoka | Niska |
| **Wykrywanie nietypowych błędów** | Niskie | Niskie | Wysokie |

---

| Kryterium | pytest | Behave (BDD) | Testowanie właściwościowe |
|-----------|--------|--------------|---------------------------|
| **Pokrycie przypadków brzegowych** | Ręczne | Ręczne | Automatyczne |
| **Szybkość pisania testów** | Szybkie | Wolniejsze | Średnie |
| **Dokumentacja wymagań** | Zależy od umiejętności zespołu | Bardzo dobra | Słaba |

---

## Kiedy stosować które podejście?

**pytest:**
* Testowanie jednostkowe komponentów
* Weryfikacja konkretnych przypadków
* Refaktoryzacja kodu

**Behave (BDD):**
* Testowanie funkcjonalności systemu
* Dokumentacja wymagań
* Współpraca z biznesem

**Testowanie właściwościowe:**
* Algorytmy i funkcje matematyczne
* Przetwarzanie danych i tekstu
* Nietypowe przypadki brzegowe

---

## Wzorzec Assert Object

https://mikulskibartosz.name/assert-object-pattern

```python
assert_that(order)\
	.has_item_count(3)\
	.includes_product("Laptop", 1)\
	.includes_product("Mouse", 2)\
	.has_total_price(936.0)  # (1000 + 2*20) * 0.9
```

---

## ZADANIE 6 (30 min)

Używając `pytest` zaimplementuj testy dla klasy `TodoList` pozwalającej na:
* dodawanie zadań
* usuwanie zadań
* oznaczanie zadań jako wykonane
* zwrócenie listy niewykonanych zadań
* zwrócenie listy wszystkich zadań i ich statusów

Użyj Assert Object!

---

## ZADANIE 7 (30 min)

Używając `behave` zaimplementuj testy dla klasy `TodoList` pozwalającej na:
* dodawanie zadań
* usuwanie zadań
* oznaczanie zadań jako wykonane
* zwrócenie listy niewykonanych zadań
* zwrócenie listy wszystkich zadań i ich statusów

---

## ZADANIE 8 (30 min)

Używając `hypothesis` zaimplementuj testy dla struktyry danych `set` testując operację łączenia zbiorów i jej właściwości:
* dodanie instniejącego elementu nie zmienia zbioru
* dodanie nowego elementu zwiększa zbiór o 1
* łączenie zbioru z pustym zbiorem nie zmienia zbioru
* łączenie zbioru z samym sobą nie zmienia zbioru
* przemienność
* łączność

---

## Czym jest pakiet Pythonowy?

* **Moduł** - pojedynczy plik .py
* **Pakiet** - katalog z plikiem `__init__.py`
* **Dystrybucja** - pakiet gotowy do instalacji przez pip

**Formaty dystrybucji:**
* **.whl** (wheel) - Nowoczesny, preferowany format
* **.tar.gz** (sdist) - Archiwum źródeł

---

## Po co publikować pakiety?

* **Współdzielenie kodu** z innymi
* **Zarządzanie zależnościami**
* **Łatwa instalacja** `pip install moj-pakiet`
* **Kontrola wersji** kodu
* **Organizacja projektu**
* **Wielokrotne użycie** kodu

---

## Tworzenie nowego pakietu

```bash
# Inicjalizacja nowego projektu
poetry new moj-super-pakiet
cd moj-super-pakiet
```

Utworzona struktura:
```
moj-super-pakiet/
│
├── moj_super_pakiet/
│   └── __init__.py
│
├── tests/
│   ├── __init__.py
│   └── test_moj_super_pakiet.py
│
├── pyproject.toml
└── README.md
```

---

## Plik konfiguracyjny pyproject.toml

```toml
[tool.poetry]
name = "moj-super-pakiet"
version = "0.1.0"
description = "Mój pierwszy pakiet Pythonowy"
authors = ["Twoje Imię <twoj.email@przykład.com>"]
readme = "README.md"
packages = [{include = "moj_super_pakiet"}]

[tool.poetry.dependencies]
python = "^3.8"

[tool.poetry.group.dev.dependencies]
pytest = "^7.0.0"

[build-system]
requires = ["poetry-core"]
build-backend = "poetry.core.masonry.api"
```

---

## Dodanie kodu do pakietu

Tworzymy nowy plik `calculator.py` w katalogu pakietu:

```python
def add(a, b):
    """Dodaje dwie liczby."""
    return a + b

def subtract(a, b):
    """Odejmuje b od a."""
    return a - b

def multiply(a, b):
    """Mnoży dwie liczby."""
    return a * b

def divide(a, b):
    """Dzieli a przez b."""
    if b == 0:
        raise ValueError("Nie można dzielić przez zero!")
    return a / b
```

---

## Aktualizacja __init__.py

```python
"""Prosty pakiet z funkcjami matematycznymi."""

from .calculator import add, subtract, multiply, divide

__version__ = '0.1.0'
```

Ten plik określa, które funkcje będą dostępne bezpośrednio z pakietu:

```python
import moj_super_pakiet
moj_super_pakiet.add(3, 5)  # 8
```

---

## Budowanie pakietu za pomocą Poetry

```bash
# Budowanie pakietu (tworzy pliki .whl i .tar.gz)
poetry build
```

Katalog `dist/` będzie zawierał:
- `moj_super_pakiet-0.1.0-py3-none-any.whl` (wheel)
- `moj-super-pakiet-0.1.0.tar.gz` (źródła)

---

## Instalacja pakietu lokalnie

```bash
# Utworzenie nowego środowiska wirtualnego
python -m venv ../test-env
source ../test-env/bin/activate  # Linux/Mac
# lub
# ..\test-env\Scripts\activate  # Windows

# Instalacja z pliku wheel
pip install dist/moj_super_pakiet-0.1.0-py3-none-any.whl
```

---

## Testowanie zainstalowanego pakietu

```python
# Uruchom Pythona
python

# W interpreterze Python:
>>> import moj_super_pakiet
>>> moj_super_pakiet.add(3, 5)
8
>>> moj_super_pakiet.divide(10, 2)
5.0
```

---

## Przygotowanie do publikacji

1. Utwórz konta:
   - TestPyPI: https://test.pypi.org/account/register/
   - PyPI: https://pypi.org/account/register/

2. Skonfiguruj Poetry:
   ```bash
   # Dla TestPyPI
   poetry config repositories.testpypi https://test.pypi.org/legacy/
   poetry config http-basic.testpypi [username] [password]

   # Dla PyPI
   poetry config http-basic.pypi [username] [password]

   # Lub token
   poetry config pypi-token.pypi [your-api-token]

   ```

---

## Publikowanie w TestPyPI

```bash
# Publikowanie w TestPyPI
poetry publish -r testpypi
```

**Testowanie pakietu z TestPyPI:**
```bash
# Utworzenie nowego środowiska
python -m venv ../test-env2
source ../test-env2/bin/activate  # Linux/Mac

# Instalacja z TestPyPI
pip install -i https://test.pypi.org/simple/ moj-super-pakiet
```

---

## Publikowanie w PyPI

```bash
# Budowanie i publikowanie w PyPI
poetry publish --build
```

**Sprawdzenie pakietu na PyPI:**

Wejdź na stronę: https://pypi.org/project/moj-super-pakiet/

**Instalacja z PyPI:**
```bash
pip install moj-super-pakiet
```

---

## Aktualizacja pakietu

1. Zmień wersję ręcznie w `pyproject.toml`:
   ```toml
   [tool.poetry]
   version = "0.1.1"
   ```

2. Lub użyj komendy Poetry:
   ```bash
   poetry version patch  # 0.1.0 -> 0.1.1
   poetry version minor  # 0.1.0 -> 0.2.0
   poetry version major  # 0.1.0 -> 1.0.0
   ```
3. Zmień wersję w `__init__.py`:

4. Opublikuj nową wersję:
   ```bash
   poetry publish --build
   ```

---

## Dobre praktyki

* **Unikalność nazwy** pakietu
* **Dokumentacja** w README.md
* **[Wersjonowanie semantyczne](https://semver.org/)** (MAJOR.MINOR.PATCH)
* **Testy jednostkowe**
* **Licencja**
* **Jasna struktura** projektu
* **Changelog**

---

## Dołączanie modeli ML do pakietu

Możemy dystrybuować wytrenowane modele ML w naszym pakiecie:

1. **Zapisanie modelu** używając joblib:
   ```python
   joblib.dump(model, 'moj_super_pakiet/models/model.joblib')
   ```

2. **Struktura pakietu z modelem:**
   ```
   moj_super_pakiet/
   ├── __init__.py
   ├── models/
   │   ├── __init__.py
   │   └── model.joblib
   └── model_utils.py
   ```

3. **Uwzględnienie plików binarnych w pyproject.toml:**
   ```toml
   [tool.poetry]
   # ...
   include = ["moj_super_pakiet/models/*.joblib"]
   ```

---

## Funkcje dostępowe do modelu

```python
import joblib
import importlib.resources as pkg_resources
from . import models

def load_model():
    """Ładuje wytrenowany model."""
    with pkg_resources.path(models, 'model.joblib') as model_path:
        model = joblib.load(str(model_path))
    return model

def predict(features):
    """Dokonuje predykcji używając modelu."""
    model = load_model()
    return model.predict([features])[0]
```

---

## Alternatywa dla dużych modeli

Dla dużych modeli (>100MB) lepiej pobierać je przy pierwszym użyciu:

```python
def load_model():
    """Ładuje model, pobierając go jeśli potrzeba."""
    os.makedirs(MODEL_PATH, exist_ok=True)
    model_file = os.path.join(MODEL_PATH, "model.joblib")

    if not os.path.exists(model_file):
        print("Pobieranie modelu...")
        response = requests.get(MODEL_URL)
        with open(model_file, "wb") as f:
            f.write(response.content)

    return joblib.load(model_file)
```

---

## Budowanie CLI

1. Tworzymy plik `__main__.py` w katalogu pakietu.

2. Plik zawiera konfigurację argparse, click, itp.

3. Dodajemy skrypt do pyproject.toml:

```
[tool.poetry.scripts]
iris-classifier = "sages_kalkulator.__main__:main"
```

---

## Użycie CLI

```bash
# Użycie funkcji jako modułu
python -m sages_kalkulator --sepal-length 5.1 --sepal-width 3.5 --petal-length 1.4 --petal-width 0.2

# Użycie CLI
iris-classifier --sepal-length 5.1 --sepal-width 3.5 --petal-length 1.4 --petal-width 0.2
```

---

## Podsumowanie

1. **Budowanie pakietu** tworzy pliki dystrybucyjne
2. **Lokalna instalacja** pozwala testować pakiet
3. **TestPyPI** służy do testowania publikacji
4. **PyPI** to oficjalne repozytorium dla wszystkich
5. **Aktualizacje** wymagają zmiany numeru wersji
6. **Modele ML** można dołączać do pakietów lub pobierać zewnętrznie

---

## ZADANIE 9 (45 minut)

1. Pobierz zbiór danych [California Housing](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_california_housing.html)
2. Wytrenuj model regresji
3. Utwórz pakiet z modelem i CLI
4. (Opcjonalnie) Opublikuj pakiet na PyPI
5. W nowym środowisku wirtualnym zainstaluj pakiet
6. Użyj pakietu do predykcji

```bash
california-housing --med_inc 123 --house_age 5 ...
```

7. (Usuń pakiet z repozytorium PyPI)

Zadanie można wykonać bez podziału notebooka na mniejsze pliki.

---

## Czym jest BentoML?

* Framework do **pakowania** i **wdrażania** modeli ML jako serwisów
* Umożliwia **standaryzację** procesu deploymentu modeli
* Wspiera **różne frameworki ML** (scikit-learn, PyTorch, TensorFlow, XGBoost...)
* Zapewnia **automatyczne API** (REST, gRPC)
* Obsługuje **przetwarzanie wsadowe** dla wydajności
* Integruje się z **kontenerami Docker** i **Kubernetes**

---

## Architektura BentoML 1.4+

* **Model Store** - repozytorium modeli
* **Service** - definicja serwisu API
* **Bento** - pakiet z modelem, serwisem i zależnościami
* **Server** - serwer obsługujący żądania API

---

## Instalacja i konfiguracja

```bash
# Instalacja BentoML
pip install "bentoml>=1.4.0"

# Dodatkowe zależności
pip install scikit-learn pandas numpy

# Sprawdzenie wersji
bentoml --version
```

---

## Trenowanie i zapisywanie modelu

```python
import bentoml
from sklearn.ensemble import RandomForestClassifier

# Trenowanie modelu
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Zapisanie modelu w BentoML
model_tag = bentoml.sklearn.save_model(
    "iris_classifier",
    model,
    signatures={
        "predict": {"batchable": True, "batch_dim": 0},
        "predict_proba": {"batchable": True, "batch_dim": 0}
    },
    metadata={"accuracy": model.score(X_test, y_test)}
)

print(f"Model zapisany: {model_tag}")
```

---

## Modele BentoML

```bash
bentoml models list
```

---

## Tworzenie serwisu BentoML

```python
# Model danych wejściowych
class IrisFeatures(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

# Mapowanie kodów klas na nazwy gatunków
SPECIES = {0: 'setosa', 1: 'versicolor', 2: 'virginica'}

# Definicja serwisu za pomocą dekoratora
@bentoml.service(
    name="iris_classifier_service",
)
class IrisClassifierService:

    def __init__(self):
        self.model = bentoml.models.get("iris_classifier:latest")
        self.model = self.model.load_model()
```

---

## Definiowanie API serwisu

```python
@bentoml.api()
def predict(self, iris_features: IrisFeatures):
	"""
	Przewiduje gatunek irysa na podstawie podanych cech.
	"""
	feature_array = np.array([
		[
			iris_features.sepal_length,
			iris_features.sepal_width,
			iris_features.petal_length,
			iris_features.petal_width
		]
	])

	# Wykonanie predykcji
	pred_class = self.model.predict(feature_array)
	pred_proba = self.model.predict_proba(feature_array)

	# Uzyskanie nazwy gatunku i pewności
	species = SPECIES[pred_class[0]]
	confidence = float(pred_proba[0][pred_class[0]])

	return {"species": species, "confidence": confidence}
```

---

## API wsadowe (batch)

```python
@bentoml.api()
def predict_batch(self, features_batch: pd.DataFrame):
	"""
	Przewiduje gatunki irysów dla wielu przykładów naraz.
	"""
	# Wykonanie predykcji wsadowej
	pred_classes = self.model.predict(features_batch)
	pred_probas = self.model.predict_proba(features_batch)

	# Przygotowanie odpowiedzi
	results = []
	for i, pred_class in enumerate(pred_classes):
		species = SPECIES[pred_class]
		confidence = float(pred_probas[i][pred_class])
		results.append({"species": species, "confidence": confidence})

	return {"predictions": results}
```

---

## Uruchamianie serwisu lokalnie

```bash
# Uruchomienie serwisu z automatycznym przeładowaniem
bentoml serve service:IrisClassifierService --reload

# Serwis dostępny pod adresem:
# http://localhost:3000
```

---

## Przykładowe zapytania

```json
{
	"iris_features": {
	  "sepal_length": 1,
	  "sepal_width": 2,
	  "petal_length": 3,
	  "petal_width": 5
	}
  }
```

```json
{
	"features_batch": [
	  {
		"sepal_length": 1,
		"sepal_width": 2,
		"petal_length": 3,
		"petal_width": 5
	  },
	  {
		"sepal_length": 1,
		"sepal_width": 2,
		"petal_length": 3,
		"petal_width": 5
	  }
	]
  }
```

---

## Tworzenie bentofile.yaml

```yaml
service: "service:IrisClassifierService"
description: "Klasyfikator gatunków irysów"
labels:
  owner: Bartosz Mikulski
  project: iris_classification
include:
  - "*.py"
python:
  packages:
    - scikit-learn
    - numpy
    - pandas
    - pydantic
models:
  - iris_classifier:latest
```

---

## Budowanie Bento

```bash
# Budowanie Bento
bentoml build

# Wyświetlenie listy Bento
bentoml list

# Wyświetlenie informacji o konkretnym Bento
bentoml get iris_classifier_service:latest
```

Wynik budowania:
```
Successfully built Bento(tag="iris_classifier_service:j2xxxxx")
```

---

## Budowanie kontenerów Docker

```bash
# Budowanie obrazu Docker z Bento
bentoml containerize iris_classifier_service:latest

# Określenie niestandardowego tagu
bentoml containerize iris_classifier_service:latest \
  -t iris_classifier:v1
```

Wynik:
```
Successfully built Docker image "iris_classifier_service:latest"
```

---

## Uruchamianie kontenera Docker

```bash
# Uruchomienie kontenera z mapowaniem portu 3000
docker run -p 3000:3000 iris_classifier_service:latest

# Sprawdzenie działających kontenerów
docker ps

# Zatrzymanie kontenera
docker stop <container_id>
```

---

## Testowanie API - pojedyncze żądanie

```bash
# Wysłanie pojedynczego żądania za pomocą curl
curl -X POST \
  http://localhost:3000/predict \
-H "Content-Type: application/json" \
-d '{
	"iris_features": {
	  "sepal_length": 1,
	  "sepal_width": 2,
	  "petal_length": 3,
	  "petal_width": 5
	}
  }'
```

Odpowiedź:
```json
{"species": "virginica", "confidence": 1.0}
```

---

## Testowanie API - żądania wsadowe

```bash
# Wysłanie żądania wsadowego
curl -X POST \
  http://localhost:3000/predict_batch \
  -H "Content-Type: application/json" \
  -d '{
	"features_batch": [
	  {
		"sepal_length": 1,
		"sepal_width": 2,
		"petal_length": 3,
		"petal_width": 5
	  },
	  {
		"sepal_length": 1,
		"sepal_width": 2,
		"petal_length": 3,
		"petal_width": 5
	  }
	]
  }'
```

Odpowiedź:
```json
{
  "predictions": [
    {"species": "virginica", "confidence": 1.0},
    {"species": "virginica", "confidence": 1.0}
  ]
}
```

---

## Dokumentacja Swagger API

* BentoML automatycznie generuje dokumentację Swagger

![Swagger UI](https://docs.bentoml.org/en/latest/_images/swagger-ui.png)

---

## Zadanie 10 (45 min)

1. Wytrenuj model klasyfikacji zbioru [Palmer Penguins](https://allisonhorst.github.io/palmerpenguins/)
2. Przygotuj usługę BentoML z modelem i API
3. Przetestuj usługę lokalnie
4. Stwórz obraz Docker z usługą.
5. Uruchom i przetestuj usługę w kontenerze Docker

```python
from sklearn.datasets import fetch_openml
df = fetch_openml(data_id=42585)
df = df['frame']
```

Podpowiedź: Encoder również trzeba zapisać w BentoML.

---

## Streamlit i REST API: Tworzenie interfejsu do modeli ML

---

## REST API - podstawy

* **REST API** to interfejs komunikacji między systemami
* Model ML w kontenerze BentoML wystawia **REST API**
* Używamy **HTTP** do komunikacji (GET, POST, PUT, DELETE)
* Dane przesyłane są najczęściej w formacie **JSON**

[HTTP](https://http.dev/)

---

## Requests - wprowadzenie

```python
import requests
import json

# Podstawowe zapytanie GET
response = requests.get("https://api.example.com/data")
print(f"Status: {response.status_code}")
print(f"Zawartość: {response.text}")

# Zapytanie POST z danymi JSON
data = {"key": "value"}
response = requests.post(
    "https://api.example.com/submit",
    headers={"Content-Type": "application/json"},
    data=json.dumps(data)
)

# Przetwarzanie odpowiedzi
if response.status_code == 200:
    result = response.json()  # Dekodowanie JSON
    print(f"Wynik: {result}")
```

---

## Komunikacja z kontenerem BentoML

```python
import requests
import json

def predict_iris(features):
    """Wywołuje model ML w kontenerze BentoML."""

    # Adres API kontenera BentoML
    api_url = "http://localhost:3000/predict"

    # Dane w formacie JSON
    headers = {"Content-Type": "application/json"}

    try:
        # Wysłanie zapytania POST
        response = requests.post(
            api_url,
            headers=headers,
            data=json.dumps(features),
            timeout=10
        )

        # Sprawdzenie odpowiedzi
        response.raise_for_status()  # Rzuci wyjątek przy błędzie HTTP
        return response.json()

    except requests.exceptions.RequestException as e:
        print(f"Błąd API: {e}")
        return None
```

---

## Obsługa błędów API

```python
try:
    response = requests.post(api_url, json=data)

    if response.status_code == 200:
        result = response.json()
        print("Sukces:", result)
    elif response.status_code == 400:
        print("Błędne dane:", response.text)
    elif response.status_code == 404:
        print("API nie znalezione")
    elif response.status_code == 500:
        print("Błąd serwera:", response.text)

except requests.exceptions.ConnectionError:
    print("Błąd połączenia: Sprawdź czy serwer działa")
except requests.exceptions.Timeout:
    print("Timeout: Serwer nie odpowiada")
except requests.exceptions.RequestException as e:
    print(f"Inny błąd: {e}")
```

---

## Czym jest Streamlit?

* Biblioteka Python do **tworzenia aplikacji webowych**
* Idealny do szybkiego tworzenia **interfejsów dla ML/AI**
* Kod w **czystym Pythonie** (bez HTML/CSS/JavaScript)
* Interaktywne **komponenty UI** z minimalistycznym kodem
* **Automatyczne odświeżanie** przy zmianach kodu
* Łatwe **wdrażanie i udostępnianie** aplikacji

---

## Uruchamianie Streamlit

```bash
streamlit run frontend.py
```

---

## Prosta aplikacja Streamlit

```python
import streamlit as st

# Tytuł i opis
st.title("Moja pierwsza aplikacja Streamlit")
st.write("To jest prosty interfejs do testowania modelu ML.")

# Sidebar - panel boczny
st.sidebar.header("Parametry")
param = st.sidebar.slider("Wybierz wartość", 0, 100, 50)

# Wyświetlenie wybranego parametru
st.write(f"Wybrana wartość: {param}")

# Przycisk akcji
if st.button("Kliknij mnie"):
    st.success("Przycisk został kliknięty!")
```

---

## Komponenty wejściowe

```python
# Tekst
name = st.text_input("Imię")
desc = st.text_area("Opis")

# Liczbowe
age = st.number_input("Wiek", min_value=0, max_value=120)
height = st.slider("Wzrost (cm)", 50, 250, 170)

# Wybór
option = st.selectbox("Opcja", ["A", "B", "C"])
options = st.multiselect("Wiele opcji", ["X", "Y", "Z"])

# Daty i pliki
date = st.date_input("Data")
file = st.file_uploader("Plik", type=["csv", "txt"])

# Przyciski
st.button("Zwykły przycisk")
st.checkbox("Zaznacz mnie")
```

---

## Układ strony

```python
# Kolumny
col1, col2 = st.columns(2)
with col1:
    st.write("Kolumna 1")
with col2:
    st.write("Kolumna 2")

# Zakładki
tab1, tab2 = st.tabs(["Karta 1", "Karta 2"])
with tab1:
    st.write("Zawartość karty 1")

# Kontenery
with st.container():
    st.write("Pogrupowane elementy")

# Expander - rozwijana sekcja
with st.expander("Rozwiń mnie"):
    st.write("Treść ukryta domyślnie")
```

---

## Integracja Streamlit z API

```python
import streamlit as st
import requests
import json

API_URL = "http://localhost:3000/predict"

st.title("Klasyfikator Irysów")

# Formularz do wprowadzania danych
with st.form("iris_form"):
    sepal_length = st.slider("Długość działki", 4.0, 8.0, 5.4)
    sepal_width = st.slider("Szerokość działki", 2.0, 4.5, 3.4)
    petal_length = st.slider("Długość płatka", 1.0, 7.0, 4.7)
    petal_width = st.slider("Szerokość płatka", 0.1, 2.5, 1.5)

    submit = st.form_submit_button("Przewidź gatunek")

if submit:
    # Przygotowanie danych
    data = {
        "sepal_length": sepal_length,
        "sepal_width": sepal_width,
        "petal_length": petal_length,
        "petal_width": petal_width
    }

    # Wywołanie API
    with st.spinner("Przetwarzanie..."):
        try:
            response = requests.post(API_URL, json=data)
            result = response.json()
            st.success(f"Gatunek: {result['species']}")
        except Exception as e:
            st.error(f"Błąd: {e}")
```

---

## Formularze z walidacją

```python
with st.form("data_form"):
    # Pola formularza
    name = st.text_input("Nazwa")
    email = st.text_input("Email")
    age = st.number_input("Wiek", min_value=0, max_value=120)

    # Przycisk submit
    submit = st.form_submit_button("Zapisz")

if submit:
    # Walidacja danych
    errors = []

    if not name:
        errors.append("Nazwa jest wymagana")

    if not email or "@" not in email:
        errors.append("Email jest nieprawidłowy")

    if age < 18:
        errors.append("Wiek musi być co najmniej 18 lat")

    # Wyświetlenie błędów lub zapisanie danych
    if errors:
        for error in errors:
            st.error(error)
    else:
        st.success("Dane zapisane pomyślnie!")
```

---

## Wyświetlanie obrazów

```python
# 1. Obraz z pliku lokalnego
st.image("lokalne_zdjecie.jpg", caption="Lokalny obraz")

# 2. Obraz z URL
from PIL import Image
import requests
from io import BytesIO

image_url = "https://przyklad.pl/obraz.jpg"
response = requests.get(image_url)
image = Image.open(BytesIO(response.content))
st.image(image, caption="Obraz z URL", width=300)
```

---

## Tworzenie wykresów

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Dane przykładowe
data = np.random.randn(20, 3)
df = pd.DataFrame(data, columns=['A', 'B', 'C'])

# 1. Wbudowane wykresy Streamlit
st.line_chart(df)
st.bar_chart(df)
st.area_chart(df)

# 2. Matplotlib
fig, ax = plt.subplots()
ax.scatter(df['A'], df['B'], c=df['C'])
ax.set_title("Wykres")
st.pyplot(fig)
```

---

## ZADANIE 11 (30 min)

Przygotuj aplikację Streamlit do obsługi modelu przygtowanego w zadaniu 10.

Po klasyfikacji pingwina, wyświetl nazwę gatunku oraz zdjęcie.

Użyj `requests` do obsługi API BentoML.

---

# Implementacja systemów AI:

## Optymalizacja, wersjonowanie

---

# Zarządzanie eksperymentami z MLflow

---

## Wprowadzenie: Problem eksperymentów ML

- Jak śledzić parametry modeli?
- Jak porównywać wyniki różnych wersji?
- Jak zapewnić reprodukowalność?
- Jak dzielić się wynikami w zespole?
- Jak zarządzać wieloma wersjami modeli?

---

## MLflow - platforma do zarządzania cyklem życia ML

- Open-source
- Niezależna od bibliotek ML
- Modularna architektura
- Prosta integracja
- Wspiera Python, R, Java i inne języki

---

## Główne komponenty MLflow

- **MLflow Tracking** - śledzenie eksperymentów i wyników
- **MLflow Projects** - pakowanie kodu ML
- **MLflow Models** - pakowanie modeli ML
- **MLflow Model Registry** - zarządzanie cyklem życia modeli (wersjonowanie, deployment)

---

## MLflow Tracking

- Śledzenie parametrów modelu
- Rejestrowanie metryk wydajności
- Zapisywanie artefaktów (wykresy, pliki)
- Organizacja eksperymentów
- Interfejs użytkownika (UI) do analizy

---

## Instalacja i konfiguracja

```bash
# Instalacja
pip install mlflow

# Uruchomienie serwera UI
mlflow ui
```

Domyślny adres: http://localhost:5000

---

## Podstawowa struktura kodu z MLflow

```python
import mlflow

# Rozpocznij eksperyment
mlflow.set_experiment("Nazwa eksperymentu")

with mlflow.start_run():
    # Zaloguj parametry
    mlflow.log_param("param1", value1)

    # Zaloguj metryki
    mlflow.log_metric("accuracy", accuracy)

    # Zapisz model
    mlflow.sklearn.log_model(model, "model")

    # Zapisz artefakt
    mlflow.log_artifact("plik.png")
```

---

## Śledzenie eksperymentów w praktyce

```python
import mlflow
import mlflow.sklearn
from sklearn.ensemble import RandomForestRegressor

with mlflow.start_run(run_name="Eksperyment RF"):
    # Parametry
    params = {"n_estimators": 100, "max_depth": 5}
    mlflow.log_params(params)

    # Trenowanie modelu
    rf = RandomForestRegressor(**params)
    rf.fit(X_train, y_train)

    # Logowanie wyników
    train_score = rf.score(X_train, y_train)
    test_score = rf.score(X_test, y_test)

    mlflow.log_metric("train_r2", train_score)
    mlflow.log_metric("test_r2", test_score)

    # Zapisanie modelu
    mlflow.sklearn.log_model(rf, "model")
```

---

## Zapisywanie własnych metryk

```python
from sklearn.metrics import mean_squared_error, r2_score

# Obliczenie różnych metryk
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

# Logowanie metryk
mlflow.log_metric("mse", mse)
mlflow.log_metric("r2", r2)
```

---

## Zapisywanie artefaktów

```python
import matplotlib.pyplot as plt
import numpy as np

# Tworzenie wykresu
plt.figure(figsize=(10, 6))
plt.scatter(y_test, y_pred)
plt.plot([min(y_test), max(y_test)],
         [min(y_test), max(y_test)], 'r--')
plt.xlabel('Wartości rzeczywiste')
plt.ylabel('Predykcje')
plt.title('Rzeczywiste vs. Predykcje')

# Zapisanie wykresu
plt.savefig("predictions_plot.png")
mlflow.log_artifact("predictions_plot.png")
```

---

## Ładowanie modelu z MLflow

```python
# Bezpośrednio po eksperymencie
model_uri = mlflow.get_artifact_uri("model")
loaded_model = mlflow.sklearn.load_model(model_uri)

# Lub z konkretnego eksperymentu
run_id = "abcdef123456789"
model_uri = f"runs:/{run_id}/model"
loaded_model = mlflow.sklearn.load_model(model_uri)

# Z Model Registry
model_name = "RandomForestRegressor"
version = 2
model = mlflow.sklearn.load_model(
    f"models:/{model_name}/{version}"
)
```

---

## ZADANIE 12 (30 min)

Wykorzystaj zbiór danych Palmer Penguins.

Zaimplementuj prosty potok uczenia maszynowego:

1. Podział danych na zbiory treningowy i testowy
2. Trenowanie modelu Random Forest z różnymi hiperparametrami
3. Ewaluacja modelu na zbiorze testowym

Śledź eksperymenty używając MLflow:

1. Utwórz eksperyment o nazwie "Palmer Penguins-Klasyfikacja"
2. Wykonaj minimum 5 uruchomień z różnymi hiperparametrami
3. Zapisz parametry, metryki i model (oraz encoder!) w każdym uruchomieniu
4. Zapisz sygnaturę modelu i przykładowe dane wejściowe

---

## MLflow Projects

- Format do pakowania kodu ML
- Definicja środowiska (conda, virtualenv)
- Parametryzowane punkty wejścia
- Reprodukowalność w różnych środowiskach

---

## Struktura projektu MLflow

```
projekt-ml/
├── MLproject         # Definicja projektu
├── conda.yaml        # Środowisko conda
├── train.py          # Skrypt treningowy
└── evaluate.py       # Skrypt ewaluacyjny
```

---

## Plik MLproject

```yaml
name: przykładowy-projekt

conda_env: conda.yaml

entry_points:
  main:
    parameters:
      alpha: {type: float, default: 0.5}
      l1_ratio: {type: float, default: 0.1}
    command: "python train.py --alpha {alpha} --l1_ratio {l1_ratio}"

  evaluate:
    parameters:
      run_id: {type: string}
    command: "python evaluate.py --run-id {run_id}"
```

---

## Uruchamianie projektu MLflow

```bash
# Lokalne uruchomienie
mlflow run ./projekt-ml -P alpha=0.2

# Uruchomienie z GitHub
mlflow run https://github.com/user/projekt-ml -P alpha=0.2

# Uruchomienie w trybie bez conda
mlflow run ./projekt-ml --env-manager local -P alpha=0.2
```

---

## ZADANIE 13 (30 min)

Użyj MLFlow Project do implementacji skryptów trenujących i ewaluujących model z zadania 12.

---

## MLflow Models

- Standardowy format modeli ML
- Niezależność od bibliotek
- Łatwy deployment
- Sygnatura modelu (wejście/wyjście)
- Wsparcie dla różnych "flavors" (sklearn, pytorch, tensorflow...)

---

## Zapisywanie modelu z sygnaturą

```python
from mlflow.models.signature import infer_signature

# Generowanie sygnatury
signature = infer_signature(X_train, model.predict(X_train))

# Zapisanie modelu z sygnaturą i przykładem
mlflow.sklearn.log_model(
    model,
    "model",
    signature=signature,
    input_example=X_train[:3]
)
```

---

## Serwowanie modelu jako API

```bash
# Uruchomienie lokalnego serwera
mlflow models serve -m runs:/RUN_ID/model --port 1234
mlflow models serve -m runs:/4dafc47af883465688d7c0cc0bccb3c2/model --port 1234


# Testowanie API
curl http://127.0.0.1:1234/invocations -H 'Content-Type: application/json' -d '{"dataframe_split": {"columns": ["sepal length (cm)","sepal width (cm)","petal length (cm)","petal width (cm)"], "data": [[5.1,3.5,1.4,0.2]]}}'
```

---

## MLflow Model Registry

- Centralny rejestr modeli
- Wersjonowanie modeli
- Zarządzanie cyklem życia (staging, production, archived)
- Przejrzystość i kontrola dostępu
- Komentarze i opisy wersji

---

## Rejestrowanie modelu

```python
# Zapisanie modelu do rejestru
with mlflow.start_run():
    # Trenowanie modelu...

    # Rejestracja modelu
    mlflow.sklearn.log_model(
        model,
        "model",
        registered_model_name="RandomForestRegressor"
    )
```

```python
# Lub rejestracja istniejącego modelu
from mlflow.tracking import MlflowClient

client = MlflowClient()
client.create_registered_model("RandomForestRegressor")
```

---


## UI MLflow - główne funkcje

- Przeglądanie eksperymentów i ich parametrów
- Porównywanie wielu eksperymentów
- Wizualizacja metryk
- Przeglądanie artefaktów
- Zarządzanie modelami w Model Registry

---

## Porównywanie eksperymentów

1. Wybierz eksperymenty do porównania
2. Użyj przycisku "Compare"
3. Wybierz metrykę do wizualizacji
4. Analizuj wpływ parametrów na wyniki

---

## Organizacja eksperymentów

- Tworzenie nowych eksperymentów
  ```python
  mlflow.set_experiment("Nowy eksperyment")
  ```

- Używanie tagów
  ```python
  with mlflow.start_run():
      mlflow.set_tag("wersja", "v1")
      mlflow.set_tag("autor", "Jan Kowalski")
  ```

- Zagnieżdżone nazwy eksperymentów
  ```python
  mlflow.set_experiment("projekt/podzadanie/model")
  ```

---

## Tagowanie eksperymentów

```python
# Dodawanie tagów
with mlflow.start_run():
    mlflow.set_tag("priorytet", "wysoki")
    mlflow.set_tag("środowisko", "produkcja")
    mlflow.set_tag("dataset", "dane_2023")

# Wyszukiwanie po tagach w UI lub API
runs = mlflow.search_runs(
    filter_string="tag.priorytet = 'wysoki'"
)
```

---

## Tworzenie raportów z eksperymentów

- Eksport tabel z wynikami (CSV)
- Eksport wykresów (PNG)
- Udostępnianie linkówp do eksperymentów
- Zapisywanie widoków w UI MLflow
- Eksport definicji eksperymentów

---

## Praktyczne zastosowania MLflow

- Śledzenie wszystkich eksperymentów
- Automatyzacja eksperymentów (CI/CD)
- Współpraca w zespole
- Wdrażanie modeli
- Audyt i dokumentacja modeli
- Reprodukowalność badań

---

## Najlepsze praktyki MLflow

- Zawsze używaj `mlflow.set_experiment()` (z wyjątkiem projektów MLflow)
- Loguj wszystkie parametry i metryki
- Dodawaj tagi dla lepszej organizacji
- Używaj sygnatur dla modeli
- Używaj hierarchii eksperymentów

---

# Optymalizacja hiperparametrów

---

## Dlaczego optymalizacja hiperparametrów jest ważna?

- Hiperparametry mają kluczowy wpływ na wydajność modelu
- Nie są bezpośrednio optymalizowane podczas treningu
- Wymagają zewnętrznego procesu optymalizacji
- Ich liczba rośnie z złożonością modelu
- Prawidłowy dobór może znacząco poprawić jakość modelu
- Zły dobór może prowadzić do przeuczenia lub niedouczenia

---

## Wyzwania w optymalizacji hiperparametrów

- Duża liczba hiperparametrów do optymalizacji
- Nieznane interakcje między parametrami
- Koszt obliczeniowy ewaluacji modeli
- Nieciągłe lub niemonotoniczne przestrzenie hiperparametrów
- Różne skale i typy parametrów (liczbowe, kategoryczne)
- Kompromis między dokładnością a czasem obliczeń

---

## Podstawowe podejścia do optymalizacji

1. **Ręczny dobór** - bazujący na doświadczeniu i heurystykach
2. **Grid Search** - systematyczne przeszukiwanie siatki wartości
3. **Random Search** - losowe próbkowanie przestrzeni
4. **Bayesowska optymalizacja** - modelowanie funkcji celu i inteligentne próbkowanie
5. **Metody ewolucyjne** - inspirowane biologiczną ewolucją
6. **Gradient-based** - optymalizacja gradientowa hiperparametrów

---

## Grid Search

**Idea**: Systematyczne przeszukiwanie wszystkich kombinacji wartości z predefiniowanej siatki

**Zalety**:
- Prosta implementacja
- Deterministyczny (zawsze te same wyniki)
- Dokładne przeszukiwanie zadanej przestrzeni

**Wady**:
- Złożoność wykładnicza O(m^n)
- Nieefektywny dla dużej liczby parametrów
- Wymaga dobrego zrozumienia zakresów parametrów

---

## Grid Search - implementacja w scikit-learn

```python
from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import RandomForestClassifier

# Definicja przestrzeni hiperparametrów
param_grid = {
    'n_estimators': [50, 100, 200],
    'max_depth': [5, 10, 15, None],
    'min_samples_split': [2, 5, 10]
}

# Konfiguracja Grid Search
grid_search = GridSearchCV(
    estimator=RandomForestClassifier(),
    param_grid=param_grid,
    cv=5,
    scoring='accuracy',
    n_jobs=-1
)

grid_search.fit(X_train, y_train)

best_params = grid_search.best_params_
```

---

## Random Search

**Idea**: Losowe próbkowanie wartości z zadanych rozkładów dla każdego parametru

**Zalety**:
- Bardziej efektywny niż Grid Search dla wielu parametrów
- Lepszy dla niejednorodnych parametrów
- Można przeznaczyć budżet obliczeniowy elastycznie

**Wady**:
- Mniejsza powtarzalność wyników
- Może nie trafić w optymalne obszary

---

## Random Search - implementacja w scikit-learn

```python
from sklearn.model_selection import RandomizedSearchCV
from scipy.stats import randint, uniform

# Definicja rozkładów dla hiperparametrów
param_distributions = {
    'n_estimators': randint(50, 300),
    'max_depth': randint(3, 20),
    'min_samples_split': randint(2, 15),
    'max_features': uniform(0.1, 0.9)
}

# Konfiguracja Random Search
random_search = RandomizedSearchCV(
    estimator=RandomForestClassifier(),
    param_distributions=param_distributions,
    n_iter=100,  # liczba kombinacji do wypróbowania
    cv=5,
    scoring='accuracy',
    n_jobs=-1
)

random_search.fit(X_train, y_train)
```

---

## Integracja Grid/Random Search z MLflow

```python
import mlflow

with mlflow.start_run(run_name="RandomSearch-RF"):
    # Logowanie informacji o przeszukiwaniu
    mlflow.log_param("search_method", "RandomizedSearchCV")
    mlflow.log_param("n_iterations", 100)

    random_search.fit(X_train, y_train)

    # Logowanie najlepszych parametrów
    best_params = random_search.best_params_
    for param, value in best_params.items():
        mlflow.log_param(f"best_{param}", value)

    # Logowanie metryk
    mlflow.log_metric("best_score", random_search.best_score_)

    # Zapisanie najlepszego modelu
    mlflow.sklearn.log_model(random_search.best_estimator_,
                            "best_model")
---

## Bayesowska optymalizacja hiperparametrów

**Idea**: Modelowanie funkcji celu i inteligentne próbkowanie w obiecujących obszarach

**Zalety**:
- Wykorzystuje wiedzę z poprzednich ewaluacji
- Wymaga znacznie mniej ewaluacji modelu
- Lepszy balans między eksploracją a eksploatacją
- Lepsze wyniki przy ograniczonym budżecie

**Wady**:
- Większa złożoność implementacji
- Wymaga dodatkowych obliczeń dla modelowania

---

## Jak działa Bayesowska optymalizacja?

1. **Model zastępczy (surrogate model)** - modeluje funkcję celu
   - Najczęściej używane: procesy Gaussowskie (Gaussian Processes)
   - Alternatywy: Random Forests, TPE (Tree-structured Parzen Estimator)

2. **Funkcja akwizycji (acquisition function)** - wybiera kolejne punkty do ewaluacji

3. **Iteracyjny proces**: modeluj → wybierz punkt → oceń → aktualizuj model → powtórz

---

## Biblioteka Optuna

- Nowoczesna biblioteka Python do optymalizacji hiperparametrów
- Efektywna implementacja Bayesowskiej optymalizacji
- Wsparcie dla pruning (wczesnego zatrzymywania)
- Zaawansowane wizualizacje
- Wbudowana integracja z popularnymi frameworkami ML
- Możliwość zrównoleglenia poszukiwań
- Zapisywanie i odtwarzanie stanu optymalizacji

---

## Optuna - podstawowe pojęcia

- **Trial** - pojedyncza ewaluacja zestawu hiperparametrów
- **Study** - zbiór trials do optymalizacji
- **Sampler** - strategia wyboru hiperparametrów (np. TPESampler)
- **Pruner** - strategia wczesnego zatrzymywania prób
- **Objective function** - funkcja do optymalizacji

---

## Definiowanie przestrzeni parametrów w Optuna

```python
# Parametry liczbowe
x = trial.suggest_float('x', -10, 10)           # Jednostajnie z [-10, 10]
y = trial.suggest_float('y', 1e-5, 1e-2, log=True)  # Logarytmicznie

# Parametry całkowitoliczbowe
n = trial.suggest_int('n', 1, 100)              # Jednostajnie z [1, 100]
m = trial.suggest_int('m', 2, 32, log=True)     # Logarytmicznie

# Parametry kategoryczne
method = trial.suggest_categorical('method', ['sgd', 'adam', 'rmsprop'])

# Warunkowe parametry
if method == 'sgd':
    momentum = trial.suggest_float('momentum', 0, 1.0)
```

---

## Integracja Optuna z MLflow

```python
from optuna.integration.mlflow import MLflowCallback

# Konfiguracja MLflow callback
mlflow_callback = MLflowCallback(
    tracking_uri=mlflow.get_tracking_uri(),
    metric_name="accuracy"
)

# Utworzenie badania (study)
study = optuna.create_study(direction='maximize')

# Rozpoczęcie optymalizacji z callbackiem
study.optimize(objective, n_trials=100, callbacks=[mlflow_callback])
```

---

## Pruning w Optuna

```python
# Definiowanie funkcji celu z pruningiem
def objective(trial):
    # Parametry modelu
    params = {
        'n_estimators': trial.suggest_int('n_estimators', 50, 1000),
        'learning_rate': trial.suggest_float('learning_rate', 0.01, 0.3)
    }

    model = GradientBoostingClassifier(**params)

    # Walidacja krzyżowa z pruningiem
    for step, (train_idx, val_idx) in enumerate(cv.split(X, y)):
        X_train_cv, X_val_cv = X[train_idx], X[val_idx]
        y_train_cv, y_val_cv = y[train_idx], y[val_idx]

        model.fit(X_train_cv, y_train_cv)
        val_score = model.score(X_val_cv, y_val_cv)

        # Raportowanie wyniku do Optuna
        trial.report(val_score, step)

        # Sprawdzenie czy przerwać próbę
        if trial.should_prune():
            raise optuna.exceptions.TrialPruned()

    return val_score

# Utworzenie badania z prunerem
study = optuna.create_study(
    direction='maximize',
    pruner=optuna.pruners.MedianPruner()
)
```

---

## Wizualizacja i analiza przestrzeni hiperparametrów

**Cel**: Zrozumienie wpływu hiperparametrów na wydajność modelu

**Korzyści**:
- Identyfikacja kluczowych hiperparametrów
- Odkrywanie interakcji między parametrami
- Lepsze zrozumienie zachowania modelu
- Zawężenie przestrzeni przeszukiwania w przyszłych eksperymentach

---

## Wizualizacje w Optuna

```python
import optuna.visualization as vis

# Historia optymalizacji
vis.plot_optimization_history(study)

# Ważność parametrów
vis.plot_param_importances(study)

# Wykresy zależności celu od parametrów
vis.plot_contour(study, params=['learning_rate', 'n_estimators'])

# Wykresy równoległe
vis.plot_parallel_coordinate(study)

# Wykresy cząstkowych zależności
vis.plot_slice(study)

# Wykres rozrzutu dla optymalizacji wielocelowej
vis.plot_pareto_front(study)  # Dla optymalizacji wielocelowej
```

---

## Historia optymalizacji

- Pokazuje progres optymalizacji w czasie
- Pozwala ocenić szybkość zbieżności
- Wskazuje, czy potrzeba więcej iteracji

---

## Wykresy konturowe

- Pokazuje wartość funkcji celu dla par parametrów
- Pozwala zidentyfikować interakcje między parametrami
- Wskazuje optymalne obszary przestrzeni parametrów

---

## Wykresy równoległe współrzędnych

- Wizualizuje wiele prób w przestrzeni wielowymiarowej
- Pozwala zidentyfikować wzorce w dobrych rozwiązaniach
- Użyteczne dla porównania wielu parametrów jednocześnie

---

## Analiza wyników optymalizacji

```python
import pandas as pd

# Pobranie danych z badania Optuna
trials_df = study.trials_dataframe()

# Podstawowe statystyki
print(trials_df.describe())

# Korelacja między parametrami a wynikiem
correlation = trials_df.corr()['value']
print(correlation)

# Najlepsze próby
best_trials = trials_df.nsmallest(10, 'value')
print(best_trials)

# Analiza trendów w najlepszych próbach
plt.figure(figsize=(10, 6))
sns.pairplot(best_trials, vars=['params_learning_rate',
                               'params_n_estimators',
                               'value'])
```

---

## Najlepsze praktyki w optymalizacji hiperparametrów

1. **Zacznij od szerokiego zakresu** parametrów, potem zawężaj
2. **Używaj skali logarytmicznej** dla parametrów o dużym zakresie
3. **Ustal priorytety** - najpierw optymalizuj najważniejsze parametry
4. **Używaj cross-validation** dla bardziej wiarygodnych wyników
5. **Monitoruj czas treningu** - dodaj go jako drugą metrykę
6. **Analizuj wyniki wizualnie** - wykresy mówią więcej niż liczby
7. **Zapisuj wszystkie eksperymenty** w MLflow
8. **Stosuj early stopping** dla oszczędności czasu
9. **Zrównoleglaj próby** gdy to możliwe

---

## Zadanie 14 (45 min)

Użyj Optuna do optymalizacji hiperparametrów modelu z zadania 12.

Pamiętaj o zapisywaniu wszystkich eksperymentów w MLflow.
Zapisz również najlepszy model w Model Registry.

---

# Wersjonowanie danych i modeli z DVC

---

## Problem: Wersjonowanie w ML

- Kod to tylko część projektu ML
- Dane są często **duże** (GB/TB)
- Dane i modele **zmieniają się** w czasie
- Git nie radzi sobie z dużymi plikami
- Trudno śledzić, która wersja kodu współpracuje z którą wersją danych

---

## Typowe sytuacje

- "Ten model osiągnął 95% dokładności, ale nie pamiętam, na jakiej wersji danych był trenowany"
- "Czy możesz mi wysłać dane, które używałeś w tym eksperymencie?"
- "Mój model daje inne wyniki niż wczoraj, ale nie zmieniałem kodu..."
- "Nie mogę zreprodukować twoich wyników"
- "Próbuję wypchać 10GB danych do Gita..."

---

## Data Version Control (DVC)

- Open-source system do wersjonowania **danych, modeli i eksperymentów**
- Zbudowany **na bazie Git**
- Śledzi **zależności** między kodem, danymi i wynikami
- Zapewnia **reprodukowalność** eksperymentów
- Umożliwia tworzenie **powtarzalnych potoków**
- Działa z **dowolnymi** magazynami danych (S3, GCS, Azure, SSH, itd.)

---

## Jak działa DVC?

- Pliki .dvc zawierają metadane (md5 hashes)
- Faktyczne dane są przechowywane w cache i zdalnym magazynie
- Git śledzi pliki .dvc

---

## Typowy workflow DVC

1. Dodanie danych do śledzenia przez DVC
2. Committing plików .dvc do Git
3. Wypchanie danych do zdalnego magazynu
4. Tworzenie potoków przetwarzania danych
5. Śledzenie zmian w danych i wynikach
6. Odtwarzanie konkretnych wersji danych i modeli

---

## Instalacja DVC

```bash
# Instalacja podstawowa
pip install dvc

# Z obsługą konkretnych magazynów
pip install dvc[s3]     # dla AWS S3
pip install dvc[gs]     # dla Google Cloud Storage
pip install dvc[azure]  # dla Azure Blob Storage
pip install dvc[gdrive] # dla Google Drive

# Inicjalizacja w projekcie git
git init
dvc init
git add .dvc .dvcignore
git commit -m "Initialize DVC"
```

---

## Śledzenie danych

```bash
# Dodanie pojedynczego pliku
dvc add data/dataset.csv

# Dodanie katalogu
dvc add data/images/

# Co się dzieje?
# 1. Utworzenie dataset.csv.dvc (metadane)
# 2. Dodanie dataset.csv do .gitignore
# 3. Kopiowanie danych do .dvc/cache
# 4. Utworzenie linku do cache

# Dodanie pliku .dvc do Git
git add data/dataset.csv.dvc data/.gitignore
git commit -m "Add dataset"
```

---

## Zdalne repozytoria

```bash
# Dodanie zdalnego repozytorium (np. S3)
dvc remote add -d myremote s3://mybucket/dvcstore

# Zapisanie konfiguracji w Git
git add .dvc/config
git commit -m "Configure remote storage"

# Wypchanie danych do zdalnego magazynu
dvc push

# Pobranie danych
dvc pull
```

---

## Obsługiwane zdalne magazyny

- **Lokalne** systemy plików
- **SSH** serwery
- **Amazon S3**
- **Google Cloud Storage**
- **Azure Blob Storage**
- **Google Drive**
- **Aliyun OSS**
- **HDFS**
- i wiele innych...

---

## Śledzenie zmian

```bash
# Sprawdzenie statusu
dvc status

# Wyświetlenie zmian w danych
dvc diff

# Powrót do wcześniejszej wersji
git checkout <stara-wersja>
dvc checkout
```

---

## Potoki DVC (Pipelines)

- **Reprodukowalne** przepływy pracy
- **Automatyczne** wykrywanie zmian
- **Inkrementalne** przetwarzanie (wykonywanie tylko niezbędnych etapów)
- **Parametryzowane** eksperymenty
- **Śledzenie** metryk i wykresów

---

## Definiowanie etapów potoku

```bash
# Przetwarzanie danych
dvc stage add -n prepare \
    -d src/prepare.py -d data/raw/dataset.csv \
    -o data/processed/features.csv \
    python src/prepare.py data/raw/dataset.csv data/processed/features.csv

# Trening modelu
dvc stage add -n train \
    -d src/train.py -d data/processed/features.csv \
    -o models/model.pkl -M metrics/metrics.json \
    python src/train.py data/processed/features.csv models/model.pkl metrics/metrics.json
```

---

## Plik dvc.yaml

```yaml
stages:
  prepare:
    cmd: python src/prepare.py data/raw/dataset.csv data/processed/features.csv
    deps:
      - src/prepare.py
      - data/raw/dataset.csv
    outs:
      - data/processed/features.csv

  train:
    cmd: python src/train.py data/processed/features.csv models/model.pkl metrics/metrics.json
    deps:
      - src/train.py
      - data/processed/features.csv
    outs:
      - models/model.pkl
    metrics:
      - metrics/metrics.json:
          cache: false
```

---

## Uruchamianie potoków

```bash
# Uruchomienie całego potoku
dvc repro

# Uruchomienie konkretnego etapu
dvc repro train

# Wyświetlenie zależności
dvc dag
```

---

## Parametryzacja potoków

```yaml
# params.yaml
prepare:
  split: 0.2
  seed: 42

train:
  model: RandomForest
  n_estimators: 100
  max_depth: 5
```

```yaml
# dvc.yaml
stages:
  train:
    params:
      - train.model
      - train.n_estimators
    cmd: python train.py
    deps:
      - ...
```

```python
# W kodzie Python
with open("params.yaml") as f:
    params = yaml.safe_load(f)
model_type = params["train"]["model"]
```

---

## Metryki i wykresy

```bash
# Wyświetlenie metryk
dvc metrics show

# Porównanie metryk między wersjami
dvc metrics diff HEAD HEAD~1

# Generowanie wykresów
dvc plots show plots/confusion_matrix.csv --template confusion

# Porównanie wykresów między wersjami
dvc plots diff HEAD HEAD~1 plots/accuracy.csv --template scatter
```

---

## Eksperymenty DVC

```bash
# Uruchomienie eksperymentu z modyfikacją parametrów
dvc exp run --set-param train.n_estimators=200

# Wyświetlenie eksperymentów
dvc exp show

# Porównanie eksperymentów
dvc exp diff exp-1a2b3c exp-4d5e6f

# Zastosowanie eksperymentu (zapis parametrów w params.yaml)
dvc exp apply exp-1a2b3c
```

---

## Zalety eksperymentów DVC

- Brak potrzeby commitowania każdego eksperymentu
- Szybkie testowanie różnych parametrów
- Łatwe porównywanie wyników
- Możliwość powrotu do poprzednich eksperymentów
- Integracja z potokami DVC

---

## Integracja z MLflow

```python
import mlflow
import yaml

# Ustawienie eksperymentu
mlflow.set_experiment("DVC-Experiment")

# Odczyt parametrów z DVC
with open("params.yaml") as f:
    params = yaml.safe_load(f)

# Trening modelu z śledzeniem MLflow
with mlflow.start_run():
    # Logowanie parametrów z DVC
    for key, value in params["train"].items():
        mlflow.log_param(key, value)

    # Trenowanie modelu
    # ...

    # Logowanie metryk w MLflow
    mlflow.log_metric("accuracy", accuracy)

    # Zapisanie modelu w MLflow
    mlflow.sklearn.log_model(model, "model")

    # Zapisanie również dla DVC
    with open("metrics/metrics.json", "w") as f:
        json.dump({"accuracy": accuracy}, f)
```

---

## Współpraca przy użyciu DVC

- **Współdzielenie danych** między członkami zespołu
- **Zdalny cache** dla szybkiego dostępu
- **Importowanie danych** z innych projektów
- **Śledzenie eksperymentów** zespołu
- **Udostępnianie modeli** i wyników

---

## Importowanie danych z innych projektów

```bash
# Importowanie danych z innego projektu
dvc import https://github.com/username/project dataset.csv

# Aktualizacja zaimportowanych danych
dvc update dataset.csv.dvc
```

---

## Typowa struktura projektu z DVC

```
projekt-ml/
├── .git/                  # Repozytorium Git
├── .dvc/                  # Konfiguracja DVC
├── data/
│   ├── raw/               # Surowe dane
│   └── processed/         # Przetworzone dane
├── src/                   # Kod źródłowy
├── models/                # Modele
├── metrics/               # Metryki
├── dvc.yaml               # Definicja potoku
├── params.yaml            # Parametry
└── requirements.txt       # Zależności
```

---

## Zalety DVC

- **Lekki** - metadane zamiast faktycznych danych w Git
- **Elastyczny** - działa z dowolnymi magazynami danych
- **Integracja z Git** - wykorzystanie istniejących narzędzi
- **Reprodukowalność** - powiązanie kodu, danych i wyników
- **Inkrementalne przetwarzanie** - ponowne wykonanie tylko zmienionych etapów
- **Eksperymentowanie** - łatwe testowanie różnych parametrów
- **Współpraca** - efektywne udostępnianie danych i modeli

---

## DVC vs. inne narzędzia

| Narzędzie   | Wersjonowanie danych | Potoki | Eksperymenty | Integracja z Git |
|-------------|----------------------|--------|--------------|------------------|
| **DVC**     | ✅                  | ✅     | ✅          | ✅               |
| Git LFS     | ✅                  | ❌     | ❌          | ✅               |
| MLflow      | ❌                  | ❌     | ✅          | ❌               |
| Pachyderm   | ✅                  | ✅     | ❌          | ❌               |
| Kubeflow    | ❌                  | ✅     | ❌          | ❌               |

---

## Najlepsze praktyki

- Organizuj dane w **logiczne grupy**
- Regularnie **wypychaj dane** do zdalnego magazynu
- Używaj **parametryzacji** potoków
- Organizuj kod tak, aby odpowiadał **etapom potoku**
- Używaj znaczących **nazw dla etapów**
- Dokumentuj zmiany w danych w **komunikatach commitów**
- Integruj DVC z **systemem CI/CD**
- Łącz DVC z **narzędziami do eksperymentów** (MLflow)

---

## ZADANIE 15 (45 minut)

Przygotuj potok DVC do trenowania modelu klasyfikującego pingwiny.

Potok powinien zawierać:
1. Pobieranie danych.
2. Przygotowanie danych. Podział na zbiór treningowy i testowy oraz one-hot encoding.
3. Trenowanie modelu.

Zapisz model na dysku oraz w MLFLow.

---

## ZADANIE 16

Zbuduj obraz Dockera zawierający model klasyfikujący churn z użyciem zbioru danych [https://raw.githubusercontent.com/sharmaroshan/Churn-Modelling-Dataset/refs/heads/master/Churn_Modelling.csv](https://raw.githubusercontent.com/sharmaroshan/Churn-Modelling-Dataset/refs/heads/master/Churn_Modelling.csv).

Użyj następujących narzędzi:

1. DVC - pobieranie danych, przetwarzanie danych i trenowanie modelu, pobieranie modelu z repozytorium MLFLow i zapisywanie w formacie BentoML.
2. MLflow - śledzenie eksperymentów i zarządzanie modelami.
3. Optuna - optymalizacja hiperparametrów wewnątrz skryptu trenującego model.
4. BentoML - budowanie usługi REST API jako obraz Dockera.

---

Podpowiedź:

Pobieranie modelu z MLFLow w formacie Scikit-Learn (gotowym do zapisu z użyciem `bentoml.sklearn.save_model`)

```python
sklearn_model = mlflow.sklearn.load_model(f"models:/{model_name}/latest")
```
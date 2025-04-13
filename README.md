# Lista Komend

## Zarządzanie zależnościami

### Pyenv - Zarządzanie Wersjami Pythona

| Komenda | Opis |
|---------|------|
| `pyenv install --list` | Wyświetla listę wszystkich dostępnych wersji Pythona |
| `pyenv install 3.10.10` | Instaluje konkretną wersję Pythona |
| `pyenv global 3.10.10` | Ustawia domyślną wersję Pythona dla całego systemu |
| `pyenv local 3.10.10` | Ustawia wersję Pythona dla bieżącego katalogu |
| `pyenv versions` | Pokazuje wszystkie zainstalowane wersje Pythona |
| `pyenv version` | Pokazuje aktualnie używaną wersję Pythona |

### Pip + venv - Standardowe Środowisko Wirtualne

| Komenda | Opis |
|---------|------|
| `python -m venv env_ml` | Tworzy nowe środowisko wirtualne |
| `env_ml\Scripts\activate` (Windows) | Aktywuje środowisko wirtualne w Windows |
| `source env_ml/bin/activate` (Linux/macOS) | Aktywuje środowisko wirtualne w Linux/macOS |
| `pip install scikit-learn==1.6.1 pandas==2.2.3 matplotlib==3.10.1` | Instaluje pakiety w określonych wersjach |
| `pip install -r requirements.txt` | Instaluje pakiety z pliku requirements.txt |
| `pip freeze > requirements.txt` | Zapisuje listę zainstalowanych pakietów do pliku |
| `deactivate` | Dezaktywuje środowisko wirtualne |

### Conda - Kompleksowe Zarządzanie Środowiskami

| Komenda | Opis |
|---------|------|
| `conda create -n conda_ml python=3.10` | Tworzy nowe środowisko conda |
| `conda activate conda_ml` | Aktywuje środowisko conda |
| `conda deactivate` | Dezaktywuje środowisko conda |
| `conda env list` | Wyświetla listę wszystkich środowisk conda |
| `conda env remove -n conda_ml` | Usuwa środowisko conda |
| `conda info --envs` | Wyświetla informacje o wszystkich środowiskach conda (ścieżka do środowiska) |
| `conda install -c conda-forge scikit-learn=1.6.1 pandas=2.2.3 matplotlib=3.10.1` | Instaluje pakiety z określonego kanału |
| `conda env create -f environment.yml` | Tworzy środowisko z pliku konfiguracyjnego |
| `conda env export > environment.yml` | Eksportuje pełną konfigurację środowiska |
| `conda env export --from-history > environment_history.yml` | Eksportuje tylko bezpośrednio instalowane pakiety |

### Poetry - Nowoczesne Zarządzanie Zależnościami

| Komenda | Opis |
|---------|------|
| `poetry new ml_project` | Tworzy nowy projekt Poetry |
| `poetry init` | Tworzy plik pyproject.toml w istniejącym projekcie |
| `poetry add scikit-learn==1.6.1 pandas==2.2.3 matplotlib==3.10.1` | Dodaje pakiety do projektu |
| `poetry add --group dev pytest==7.3.1 black==23.3.0 mypy==1.3.0` | Dodaje pakiety deweloperskie do projektu |
| `poetry install --without dev` | Instaluje tylko główne zależności (bez deweloperskich) |
| `poetry shell` | Aktywuje shell w środowisku Poetry |
| `poetry run python script.py` | Uruchamia skrypt w środowisku Poetry |
| `poetry export -f requirements.txt --output requirements.txt` | Eksportuje zależności do formatu requirements.txt |
| `poetry env list` | Wyświetla listę wszystkich środowisk Poetry |
| `poetry env remove nazwa_środowiska` | Usuwa środowisko Poetry |

### UV - Szybki Instalator Pakietów

| Komenda | Opis |
|---------|------|
| `pip install uv` | Instaluje UV |
| `uv venv` | Tworzy środowisko wirtualne |
| `uv venv --python=python3.10` | Tworzy środowisko z określoną wersją Pythona |
| `uv pip install scikit-learn==1.6.1 pandas==2.2.3 matplotlib==3.10.1` | Instaluje pakiety |
| `uv pip install -r requirements.txt` | Instaluje pakiety z pliku requirements.txt |
| `uv pip freeze > requirements.txt` | Zapisuje listę zainstalowanych pakietów |

### Pliki Konfiguracyjne

#### requirements.txt (pip/uv)
```
scikit-learn==1.6.1
pandas==2.2.3
matplotlib==3.10.1
```

#### environment.yml (conda)
```yaml
name: conda_ml
channels:
  - conda-forge
  - defaults
dependencies:
  - python=3.10
  - scikit-learn=1.6.1
  - pandas=2.2.3
  - matplotlib=3.10.1
```

#### pyproject.toml (poetry)
```toml
[tool.poetry]
name = "ml_project"
version = "0.1.0"
description = "Projekt uczenia maszynowego"
authors = ["Imię Nazwisko <email@example.com>"]

[tool.poetry.dependencies]
python = "^3.10"
scikit-learn = "1.6.1"
pandas = "2.2.3"
matplotlib = "3.10.1"

[tool.poetry.group.dev.dependencies]
pytest = "^7.3.1"

[build-system]
requires = ["poetry-core>=1.0.0"]
build-backend = "poetry.core.masonry.api"
```

## Uruchamianie testów

### Uruchamianie testów pytest

| Komenda | Opis |
|---------|------|
| `pytest` | Uruchamia wszystkie testy |
| `pytest -v` | Uruchamia wszystkie testy w trybie verbose |
| `pytest -m "nazwa_tagu"` | Uruchamia testy z określonym tagiem |
| `pytest -k "nazwa_testu"` | Uruchamia określony test |
| `pytest -k "not nazwa_testu"` | Uruchamia wszystkie testy oprócz określonego testu |
| `pytest -m "not nazwa_tagu"` | Uruchamia wszystkie testy oprócz testów z określonym tagiem |

### Uruchamianie testów Behave (BDD)

| Komenda | Opis |
|---------|------|
| `behave` | Uruchamia wszystkie scenariusze testowe |
| `behave -v` | Uruchamia testy w trybie verbose (szczegółowy) |
| `behave --tags=@tag` | Uruchamia scenariusze z określonym tagiem |
| `behave --tags=-@tag` | Uruchamia wszystkie scenariusze oprócz tych z określonym tagiem |
| `behave features/nazwa.feature` | Uruchamia testy z określonego pliku feature |

## Budowanie i publikowanie pakietu

### Budowanie pakietów przy użyciu Poetry

| Komenda | Opis |
|---------|------|
| `poetry build` | Buduje paczkę dystrybucyjną (wheel i sdist) |
| `poetry version patch` | Zwiększa wersję projektu (patch, minor, major) |
| `poetry publish` | Publikuje paczkę w PyPI |
| `poetry publish --build` | Buduje i publikuje paczkę w jednym kroku |
| `poetry publish --repository testpypi` | Publikuje paczkę w TestPyPI |
| `poetry config repositories.testpypi https://test.pypi.org/legacy/` | Konfiguruje repozytorium TestPyPI |
| `poetry config pypi-token.pypi <token>` | Konfiguruje token uwierzytelniający dla PyPI |
| `poetry config pypi-token.testpypi <token>` | Konfiguruje token uwierzytelniający dla TestPyPI |

## Uruchamianie serwisu BentoML

### Zarządzanie serwisem BentoML i Docker

| Komenda | Opis |
|---------|------|
| `bentoml serve service:svc --reload` | Uruchamia serwis lokalnie z automatycznym przeładowaniem |
| `bentoml models list` | Wyświetla listę modeli BentoML |
| `bentoml list` | Wyświetla listę wszystkich serwisów i modeli |
| `bentoml get iris_classifier:latest` | Pobiera informacje o modelu BentoML |
| `bentoml containerize iris_classifier_service:latest` | Buduje kontener Docker |
| `bentoml containerize iris_classifier_service:latest -t iris_classifier:v1` | Buduje kontener Docker z określonym tagiem |
| `docker run -p 3000:3000 iris_classifier:v1` | Uruchamia serwis w kontenerze Docker |
| `docker ps` | Wyświetla listę wszystkich uruchomionych kontenerów Docker wraz z ich identyfikatorami, nazwami i statusem |
| `docker stop <container id>` | Zatrzymuje działający kontener Docker o podanym identyfikatorze (ID) |


## Zapytania przy użyciu CURL

### Testowanie API BentoML przy użyciu CURL

| Komenda | Opis |
|---------|------|
| `curl -X POST http://localhost:3000/predict -H "Content-Type: application/json" -d '{"iris_features": {"sepal_length": 1, "sepal_width": 2, "petal_length": 3, "petal_width": 5}}'` | Wysyła żądanie z obiektem iris_features |
| `curl -X POST http://localhost:3000/predict_batch -H "Content-Type: application/json" -d '{"features_batch": [{"sepal_length": 1, "sepal_width": 2, "petal_length": 3, "petal_width": 5}, {"sepal_length": 1, "sepal_width": 2, "petal_length": 3, "petal_width": 5}]}'` | Wysyła żądanie wsadowe do endpointu predict_batch |

## Uruchamianie Streamlit

| Komenda | Opis |
|---------|------|
| `streamlit run plik.py` | Uruchamia Streamlit |

## MLFLow

| Komenda | Opis |
|---------|------|
| `mlflow ui` | Uruchamia interfejs webowy MLflow |
| `mlflow run .` | Uruchamia projekt MLflow z bieżącego katalogu |
| `mlflow run . -P alpha=0.5` | Uruchamia projekt z parametrem |
| `mlflow models serve -m runs:/<run-id>/model` | Serwuje model z konkretnego uruchomienia |
| `mlflow models predict -m runs:/<run-id>/model -i dane.csv` | Wykonuje predykcję używając modelu |
| `mlflow artifacts download -u runs:/<run-id>/model -d ./downloaded_model` | Pobiera artefakty z uruchomienia |

## DVC

| Komenda | Opis |
|---------|------|
| `dvc init` | Inicjalizuje DVC w projekcie |
| `dvc add data/dataset.csv` | Dodaje plik do śledzenia przez DVC |
| `dvc remote add -d myremote s3://bucket/path` | Dodaje zdalne repozytorium |
| `dvc remote add -d myremote gdrive://folder_id` | Dodaje Google Drive jako zdalne repozytorium |
| `dvc push` | Wysyła dane do zdalnego repozytorium |
| `dvc pull` | Pobiera dane ze zdalnego repozytorium |
| `dvc stage add -n nazwa -d plik.py -o wynik.csv python plik.py` | Tworzy etap potoku, gdzie: -n określa nazwę etapu, -d definiuje zależności (pliki wejściowe), -o określa pliki wyjściowe, a po parametrach podajemy komendę do wykonania (zapisywanie metryk: -M metrics.json) |
| `dvc repro` | Uruchamia potok DVC |
| `dvc dag` | Wyświetla graf potoku |
| `dvc metrics show` | Wyświetla metryki |
| `dvc metrics diff` | Porównuje metryki między wersjami |
| `dvc exp run` | Uruchamia eksperyment |
| `dvc exp show` | Wyświetla listę eksperymentów |
| `dvc exp diff` | Porównuje eksperymenty |
| `dvc exp apply exp-1a2b3c` | Zastosowuje eksperyment (zapis parametrów w params.yaml) |
| `dvc exp run --set-param train.model.n_estimators=50` | Uruchamia eksperyment z określonym parametrem |

# Podsumowanie narzędzi używanych podczas warsztatów

## Zarządzanie zależnościami

W projektach ML zarządzanie zależnościami jest kluczowe ze względu na ścisłe wymagania wersji bibliotek, potrzebę odtwarzalności środowiska oraz współpracę w zespole.

### pip + venv
Standardowy menedżer pakietów Python z modułem do tworzenia wirtualnych środowisk. Używany do instalacji pakietów Python i izolacji projektów. Definicja zależności odbywa się poprzez plik `requirements.txt`.

### conda
Kompleksowy menedżer środowisk i pakietów, który zarządza nie tylko bibliotekami Pythona, ale również wersjami samego Pythona i zależnościami binarnymi (C, C++, CUDA). Szczególnie przydatny w projektach ML wymagających specyficznych bibliotek naukowych z komponentami niskopoziomowymi.

### poetry
Nowoczesne narzędzie do zarządzania zależnościami i publikowania pakietów. Używa pliku `pyproject.toml` do definiowania zależności, umożliwia tworzenie grup zależności (np. dev, test) oraz wspiera publikowanie własnych pakietów.

### uv
Szybki instalator pakietów Python, kompatybilny z istniejącymi formatami (requirements.txt, pyproject.toml). Znacząco przyspiesza proces instalacji pakietów, co jest istotne w dużych projektach ML z wieloma zależnościami.

## DVC (Data Version Control)

DVC to narzędzie do wersjonowania danych i modeli oraz definiowania potoków ML. Integruje się z Git, ale zamiast przechowywać duże pliki w repozytorium, śledzi metadane i przechowuje faktyczne dane w zewnętrznych magazynach (S3, GCS, lokalny dysk).

W workflow ML, DVC służy do:
- Śledzenia zmian w danych i modelach
- Definiowania potoków przetwarzania danych i trenowania modeli
- Parametryzacji eksperymentów
- Odtwarzalności wyników
- Współpracy w zespole poprzez współdzielenie danych i modeli

DVC pozwala na przyrostowe przetwarzanie - ponowne wykonanie tylko tych etapów potoku, których zależności uległy zmianie, co oszczędza czas i zasoby.

## MLflow

MLflow to platforma do zarządzania całym cyklem życia ML. Składa się z kilku komponentów:

- **MLflow Tracking**: Rejestrowanie parametrów, metryk i artefaktów eksperymentów
- **MLflow Projects**: Pakowanie kodu ML w formie możliwej do odtworzenia
- **MLflow Models**: Pakowanie modeli w standardowym formacie do wdrożenia
- **MLflow Registry**: Centralny rejestr modeli z zarządzaniem cyklem życia

W workflow ML, MLflow służy do:
- Śledzenia i porównywania wyników eksperymentów
- Zapisywania modeli w standardowym formacie
- Zarządzania wersjami modeli
- Wdrażania modeli w różnych środowiskach

MLflow integruje się z popularnymi bibliotekami ML (scikit-learn, TensorFlow, PyTorch) i może współpracować z DVC, tworząc kompletne rozwiązanie do zarządzania eksperymentami.

## BentoML

BentoML to framework do pakowania modeli ML do wdrożenia jako usługi. Umożliwia tworzenie API REST dla modeli ML i pakowanie ich jako kontenery Docker.

W workflow ML, BentoML służy do:
- Standaryzacji interfejsu modeli
- Obsługi wielu frameworków ML (scikit-learn, TensorFlow, PyTorch)
- Tworzenia serwisów API z modelami ML
- Budowania obrazów Docker gotowych do wdrożenia
- Skalowania usług ML w środowiskach produkcyjnych

BentoML upraszcza proces przejścia od eksperymentu do produkcji, zapewniając spójny interfejs dla modeli i automatyzując proces wdrażania.

## Optuna

Optuna to framework do automatycznej optymalizacji hiperparametrów. Wykorzystuje zaawansowane algorytmy przeszukiwania przestrzeni parametrów.

W workflow ML, Optuna służy do:
- Automatycznego strojenia hiperparametrów modeli
- Efektywnego przeszukiwania przestrzeni parametrów
- Wizualizacji procesu optymalizacji
- Równoległego wykonywania eksperymentów
- Integracji z popularnymi bibliotekami ML (scikit-learn, TensorFlow, PyTorch)

Optuna pozwala na definiowanie złożonych przestrzeni przeszukiwania i optymalizację wielu celów jednocześnie, co jest kluczowe w zaawansowanych projektach ML.

## Streamlit

Streamlit to framework do tworzenia interfejsów webowych dla modeli ML. Umożliwia tworzenie aplikacji ML w formie pojedynczego pliku Python, które można łatwo wdrożyć i udostępnić.

W workflow ML, Streamlit służy do:
- Tworzenia interfejsów użytkownika dla modeli ML na potrzeby demonstracji i testowania
- Wizualizacji wyników eksperymentów
- Udostępniania modeli ML w formie webowej
- Przygotowania interfejsów użytkownika na potrzeby etykietowania danych




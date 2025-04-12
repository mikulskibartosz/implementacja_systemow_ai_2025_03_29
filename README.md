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
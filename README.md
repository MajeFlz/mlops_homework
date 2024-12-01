# mlops_homework

<a target="_blank" href="https://cookiecutter-data-science.drivendata.org/">
    <img src="https://img.shields.io/badge/CCDS-Project%20template-328F97?logo=cookiecutter" />
</a>

##Как настроить

### lr3
1. Клонируйте репозиторий и перейдите в директорию проекта
	
```
git clone https://github.com/MajeFlz/mlops_homework
cd mlops_homework
git checkout homework3

```

2. Установите Poetry и зависимости проекта

```
poetry install
```

3. Активируйте виртуальное окружение Poetry
```
poetry shell
```

4. Создайте файл .env по шаблону .env.example

```
echo "MINIO_ROOT_USER=admin" >> .env
echo "MINIO_ROOT_PASSWORD=password" >> .env
```

5. Соберите и запустите Docker

```
docker-compose up --build
```
Теперь сервис доступен по локальному адресу: http://127.0.0.1:9000
И там уже будет bucket с файлом датасета

6. Запустите скрипт run_etl.py для автоматического преобразования
```
python run_etl.py
```
 ИЛИ
 
 Запустите скрипты по отдельности
```
python ./etl_scripts/scripts/download.py --bucket my-bucket --key titanic.csv --output ./data/raw/dataset_titanic.csv
python ./etl_scripts/scripts/process.py --input ./data/raw/dataset_titanic.csv --output ./data/processed/processed_dataset_titanic.csv
python ./etl_scripts/scripts/upload.py --bucket my-bucket --key processed_dataset_titanic.csv --file ./data/processed/processed_dataset_titanic.csv
 ```


### lr 2
Настройте хуки прекоммита

```
pre-commit install
```

## Project Organization

```
├── LICENSE            <- Open-source license if one is chosen
├── Makefile           <- Makefile with convenience commands like `make data` or `make train`
├── README.md          <- The top-level README for developers using this project.
├── data
│   ├── external       <- Data from third party sources.
│   ├── interim        <- Intermediate data that has been transformed.
│   ├── processed      <- The final, canonical data sets for modeling.
│   └── raw            <- The original, immutable data dump.
│
├── docs               <- A default mkdocs project; see www.mkdocs.org for details
│
├── models             <- Trained and serialized models, model predictions, or model summaries
│
├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
│                         the creator's initials, and a short `-` delimited description, e.g.
│                         `1.0-jqp-initial-data-exploration`.
│
├── pyproject.toml     <- Project configuration file with package metadata for 
│                         mlops_homework and configuration for tools like black
│
├── references         <- Data dictionaries, manuals, and all other explanatory materials.
│
├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
│   └── figures        <- Generated graphics and figures to be used in reporting
│
├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
│                         generated with `pip freeze > requirements.txt`
│
├── setup.cfg          <- Configuration file for flake8
│
└── mlops_homework   <- Source code for use in this project.
    │
    ├── __init__.py             <- Makes mlops_homework a Python module
    │
    ├── config.py               <- Store useful variables and configuration
    │
    ├── dataset.py              <- Scripts to download or generate data
    │
    ├── features.py             <- Code to create features for modeling
    │
    ├── modeling                
    │   ├── __init__.py 
    │   ├── predict.py          <- Code to run model inference with trained models          
    │   └── train.py            <- Code to train models
    │
    └── plots.py                <- Code to create visualizations
```

--------


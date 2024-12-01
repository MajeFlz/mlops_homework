import mlflow
import mlflow.sklearn
import json
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, f1_score
import os
import boto3
from dotenv import load_dotenv

def train_and_log_model(config_path: str, dataset_path: str, s3_bucket_name: str):
    load_dotenv()  # Загрузка переменных окружения из .env

    # Настройка подключения к MinIO
    s3 = boto3.client(
        's3',
        endpoint_url='http://minio:9000',  # Адрес MinIO в контейнере
        aws_access_key_id=os.getenv('MINIO_ROOT_USER'),
        aws_secret_access_key=os.getenv('MINIO_ROOT_PASSWORD'),
        region_name='us-east-1'  # Регион MinIO, может быть любым
    )
    
    # Загружаем конфиг
    with open(config_path, "r") as file:
        config = json.load(file)

    # Загружаем датасет
    data = pd.read_csv(dataset_path)

    # Предобработка данных
    data = data.drop(["Name"], axis=1, errors='ignore')
    data['Age'] = data['Age'].fillna(data['Age'].median())

    # Разделение данных на признаки и целевую переменную
    X = data.drop("Survived", axis=1)
    y = data["Survived"]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Настройка MLflow и указание S3 для артефактов
    experiment_name = "my_experiment"  # Используйте имя эксперимента

    # Проверка на существование эксперимента
    experiment = mlflow.get_experiment_by_name(experiment_name)
    if experiment is None:
        # Эксперимент не существует, создаем новый
        mlflow.create_experiment(experiment_name)

    # Устанавливаем URI для отслеживания (например, локальный сервер)
    mlflow.set_tracking_uri("http://127.0.0.1:5000")  # Убедитесь, что у вас работает сервер MLflow

    # Устанавливаем S3 как хранилище артефактов через переменные окружения
    os.environ['MLFLOW_S3_ENDPOINT_URL'] = "http://minio:9000"  # Указание на MinIO как S3 endpoint
    os.environ['AWS_ACCESS_KEY_ID'] = os.getenv('MINIO_ROOT_USER')
    os.environ['AWS_SECRET_ACCESS_KEY'] = os.getenv('MINIO_ROOT_PASSWORD')
    os.environ['AWS_DEFAULT_REGION'] = 'us-east-1'

    # Логирование модели
    with mlflow.start_run():
        for params in config["param_grid"]:
            with mlflow.start_run(nested=True):  # Вложенный запуск
                # Инициализация модели с параметрами из конфига
                model = RandomForestClassifier(
                    n_estimators=params["n_estimators"],
                    max_depth=params["max_depth"],
                    min_samples_split=params["min_samples_split"],
                    random_state=42
                )

                model.fit(X_train, y_train)
                X_test = pd.DataFrame(X_test, columns=X.columns)

                # Прогнозирование
                y_pred = model.predict(X_test)

                # Метрики
                accuracy = accuracy_score(y_test, y_pred)
                f1 = f1_score(y_test, y_pred)

                # Логирование параметров, метрик и модели
                mlflow.log_param("n_estimators", params["n_estimators"])
                mlflow.log_param("max_depth", params["max_depth"])
                mlflow.log_param("min_samples_split", params["min_samples_split"])
                mlflow.log_metric("accuracy", accuracy)
                mlflow.log_metric("f1_score", f1)
                
                # Логируем модель на S3
                model_path = f"{experiment_name}/{mlflow.active_run().info.run_id}/model"
                mlflow.sklearn.log_model(model, model_path)

                print(f"Model logged with n_estimators={params['n_estimators']}, max_depth={params['max_depth']}, min_samples_split={params['min_samples_split']}. Accuracy: {accuracy:.2f}, F1: {f1:.2f}")

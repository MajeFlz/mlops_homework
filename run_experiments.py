import os
from mlops_homework.train_and_log_model import train_and_log_model

def run_experiments():
    configs_dir = "configs"
    dataset_path = "./data/processed/processed_dataset_titanic.csv"
    s3_bucket_name = "my-bucket"  # Укажите здесь свой бакет S3

    for config_file in os.listdir(configs_dir):
        if config_file.endswith(".json"):
            config_path = os.path.join(configs_dir, config_file)
            print(f"Running experiment with config: {config_path}")
            # Передаем все три аргумента
            train_and_log_model(config_path, dataset_path, s3_bucket_name)

if __name__ == "__main__":
    run_experiments()

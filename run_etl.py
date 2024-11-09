import subprocess

def run_command(command):
    result = subprocess.run(command, shell=True)
    if result.returncode != 0:
        print(f"Ошибка при выполнении: {' '.join(command)}")
        exit(result.returncode)

if __name__ == "__main__":
    download_command = "python ./etl_scripts/scripts/download.py --bucket my-bucket --key titanic.csv --output ./data/raw/dataset_titanic.csv"
    run_command(download_command)

    process_command = "python ./etl_scripts/scripts/process.py --input ./data/raw/dataset_titanic.csv --output ./data/processed/processed_dataset_titanic.csv"
    run_command(process_command)

    upload_command = "python ./etl_scripts/scripts/upload.py --bucket my-bucket --key processed_dataset_titanic.csv --file ./data/processed/processed_dataset_titanic.csv"
    run_command(upload_command)

    print("ETL процесс завершён успешно.")

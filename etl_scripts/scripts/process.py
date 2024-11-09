import pandas as pd
import argparse

def process_data(input_path, output_path):
    df = pd.read_csv(input_path)
    
    df["Sex"] = df["Sex"].apply(lambda x: "0" if x == "female" else "1")
 
    df.to_csv(output_path, index=False)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Обработка данных")
    parser.add_argument("--input", required=True, help="Путь к входному файлу")
    parser.add_argument("--output", required=True, help="Путь к выходному файлу")
    args = parser.parse_args()
    process_data(args.input, args.output)
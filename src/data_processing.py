
import os
import pandas as pd

def load_data(data_folder):
    """
    Loads all CSV files from the data folder and returns a dictionary of DataFrames.
    """
    files = [
        "holidays_events.csv",
        "oil.csv",
        "sample_submission.csv",
        "stores.csv",
        "test.csv",
        "train.csv",
        "transactions.csv"
    ]

    data = {}
    for file in files:
        path = os.path.join(data_folder, file)
        if os.path.exists(path):
            df = pd.read_csv(path)
            # Store key as file name without extension
            data[file.split(".")[0]] = df
            print(f"Loaded {file} — Shape: {df.shape}")
        else:
            print(f"File not found: {file}")
    return data

if __name__ == "__main__":
    data_folder = os.path.join(os.getcwd(), "data")
    data = load_data(data_folder)
    print("\n--- Dataset Overview ---")
    for name, df in data.items():
        print(f"\n{name} shape: {df.shape}")
        print(df.head(2))

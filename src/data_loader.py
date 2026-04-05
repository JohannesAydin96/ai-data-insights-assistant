import pandas as pd

def load_data(file_path):
    df = pd.read_csv(file_path)
    return df


if __name__ == "__main__":
    df = load_data("data/raw/superstore.csv")

    print("First 5 rows:")
    print(df.head())

    print("\nShape:")
    print(df.shape)

    print("\nColumns:")
    print(df.columns)

    print("\nData types:")
    print(df.dtypes)

    print("\nMissing values:")
    print(df.isnull().sum())
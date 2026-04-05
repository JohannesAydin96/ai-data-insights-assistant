import pandas as pd

def load_data(file_path):
    return pd.read_csv(file_path)

def generate_basic_summary(df):
    summary = {}

    summary["num_rows"] = df.shape[0]
    summary["num_columns"] = df.shape[1]
    summary["columns"] = list(df.columns)

    summary["missing_values"] = df.isnull().sum().to_dict()

    summary["total_sales"] = float(df["Sales"].sum())
    summary["total_profit"] = float(df["Profit"].sum())
    summary["avg_sales"] = float(df["Sales"].mean())

    summary["top_categories"] = (
        df.groupby("Category")["Sales"]
        .sum()
        .sort_values(ascending=False)
        .to_dict()
    )

    summary["top_regions"] = (
        df.groupby("Region")["Sales"]
        .sum()
        .sort_values(ascending=False)
        .to_dict()
    )
    summary["missing_values"] = df.isnull().sum().to_dict()

    return summary


if __name__ == "__main__":
    df = load_data("data/raw/superstore.csv")

    summary = generate_basic_summary(df)

    print("Basic Summary:")
    print(summary)
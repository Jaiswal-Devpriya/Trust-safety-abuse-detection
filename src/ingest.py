import pandas as pd

def load_dataset():
    df = pd.read_csv("data/raw/train.csv")

    print(f"Rows: {len(df)}")
    print(f"Columns: {len(df.columns)}")

    print("\nColumn Names:")
    print(df.columns.tolist())

    print("\nSample Data:")
    print(df.head())

    return df


if __name__ == "__main__":
    load_dataset()
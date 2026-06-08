import pandas as pd

LABEL_COLS = [
    "toxic",
    "severe_toxic",
    "obscene",
    "threat",
    "insult",
    "identity_hate",
]

def normalize_dataset(input_path="data/raw/train.csv", output_path="data/processed/train_clean.csv"):
    df = pd.read_csv(input_path)

    # Basic text cleaning
    df["comment_text"] = (
        df["comment_text"]
        .fillna("")
        .astype(str)
        .str.replace("\n", " ", regex=False)
        .str.replace("\r", " ", regex=False)
        .str.strip()
    )

    # Create a list of true labels for each row
    def get_true_labels(row):
        labels = [col for col in LABEL_COLS if row[col] == 1]
        return labels if labels else ["non_abusive"]

    df["true_labels"] = df.apply(get_true_labels, axis=1)

    # Keep useful columns
    clean_df = df[["id", "comment_text", "true_labels"] + LABEL_COLS]

    clean_df.to_csv(output_path, index=False)
    print(f"Saved cleaned dataset to {output_path}")
    print(clean_df.head())

    return clean_df


if __name__ == "__main__":
    normalize_dataset()
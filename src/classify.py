import pandas as pd
from pathlib import Path

INPUT_PATH = Path("data/processed/train_clean.csv")
OUTPUT_PATH = Path("data/outputs/classified_comments.csv")

ABUSE_KEYWORDS = {
    "toxic": ["stupid", "idiot", "dumb", "hate", "trash", "loser"],
    "severe_toxic": ["kill", "die", "destroy"],
    "obscene": ["fuck", "shit", "bitch", "asshole"],
    "threat": ["i will kill", "hurt you", "attack"],
    "insult": ["idiot", "moron", "loser", "clown"],
    "identity_hate": ["racist", "terrorist", "go back", "illegal"]
}

def classify_text(text):
    text = str(text).lower()
    labels = []

    for category, keywords in ABUSE_KEYWORDS.items():
        if any(keyword in text for keyword in keywords):
            labels.append(category)

    return labels if labels else ["clean"]

def score_priority(labels):
    high_risk = {"severe_toxic", "threat", "identity_hate"}
    medium_risk = {"toxic", "obscene", "insult"}

    if any(label in high_risk for label in labels):
        return "high"
    if any(label in medium_risk for label in labels):
        return "medium"
    return "low"

def main():
    df = pd.read_csv(INPUT_PATH)

    text_col = "comment_text" if "comment_text" in df.columns else df.columns[0]

    df["predicted_labels"] = df[text_col].apply(classify_text)
    df["risk_priority"] = df["predicted_labels"].apply(score_priority)
    df["predicted_labels"] = df["predicted_labels"].apply(lambda x: ", ".join(x))

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(OUTPUT_PATH, index=False)

    print(f"Saved classified output to {OUTPUT_PATH}")

if __name__ == "__main__":
    main()
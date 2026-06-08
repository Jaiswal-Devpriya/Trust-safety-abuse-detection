import pandas as pd
from pathlib import Path

INPUT_PATH = Path("data/outputs/classified_comments.csv")

SUMMARY_PATH = Path("data/outputs/moderation_summary.csv")
ABUSE_PATH = Path("data/outputs/abuse_distribution.csv")

df = pd.read_csv(INPUT_PATH)

# Risk distribution
risk_counts = (
    df["risk_priority"]
    .value_counts()
    .reset_index()
)

risk_counts.columns = ["risk_priority", "count"]
risk_counts.to_csv(SUMMARY_PATH, index=False)

# Abuse category distribution
label_counts = {}

for labels in df["predicted_labels"]:
    for label in str(labels).split(", "):
        label_counts[label] = label_counts.get(label, 0) + 1

abuse_df = pd.DataFrame(
    label_counts.items(),
    columns=["abuse_type", "count"]
)

abuse_df = abuse_df.sort_values(
    by="count",
    ascending=False
)

abuse_df.to_csv(ABUSE_PATH, index=False)

print("\nRisk Distribution")
print(risk_counts)

print("\nAbuse Category Distribution")
print(abuse_df)

print(f"\nSaved summary to {SUMMARY_PATH}")
print(f"Saved abuse distribution to {ABUSE_PATH}")
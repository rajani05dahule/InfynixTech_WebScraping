import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("quotes_dataset.csv")

# Basic information
print("Dataset Shape:", df.shape)
print("\nColumns:")
print(df.columns)

print("\nFirst 5 Rows:")
print(df.head())

# Count quotes by author
author_counts = df["Author"].value_counts()

print("\nQuotes by Author:")
print(author_counts)

# Most frequent author
print("\nMost Frequent Author:")
print(author_counts.idxmax())
print("Quotes:", author_counts.max())

# Visualization
author_counts.head(10).plot(kind="bar")
plt.title("Top Authors by Number of Quotes")
plt.xlabel("Author")
plt.ylabel("Number of Quotes")
plt.tight_layout()

# Save chart
plt.savefig("author_chart.png")
plt.show()

print("\nChart saved as author_chart.png")
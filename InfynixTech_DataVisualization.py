import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("quotes_dataset.csv")

# Count quotes by author
author_counts = df['Author'].value_counts()

# Chart 1: Bar Chart
plt.figure(figsize=(8,5))
author_counts.plot(kind='bar')
plt.title("Number of Quotes by Author")
plt.xlabel("Author")
plt.ylabel("Count")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("bar_chart.png")
plt.show()

# Chart 2: Pie Chart
plt.figure(figsize=(7,7))
author_counts.plot(kind='pie', autopct='%1.1f%%')
plt.title("Author Distribution")
plt.ylabel("")
plt.savefig("pie_chart.png")
plt.show()

print("Charts created successfully!")
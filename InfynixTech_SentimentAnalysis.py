import pandas as pd
from textblob import TextBlob

# Load dataset
df = pd.read_csv("quotes_dataset.csv")

# Function to classify sentiment
def get_sentiment(text):
    polarity = TextBlob(str(text)).sentiment.polarity

    if polarity > 0:
        return "Positive"
    elif polarity < 0:
        return "Negative"
    else:
        return "Neutral"

# Apply sentiment analysis
df["Sentiment"] = df["Quote"].apply(get_sentiment)

# Display results
print(df[["Author", "Sentiment"]])

# Save output
df.to_csv("quotes_sentiment.csv", index=False)

# Count sentiments
print("\nSentiment Summary:")
print(df["Sentiment"].value_counts())

print("\nSentiment Analysis Completed!")
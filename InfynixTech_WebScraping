import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "http://quotes.toscrape.com"

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

quotes = []
authors = []

for quote in soup.find_all("div", class_="quote"):
    quotes.append(quote.find("span", class_="text").text)
    authors.append(quote.find("small", class_="author").text)

df = pd.DataFrame({
    "Quote": quotes,
    "Author": authors
})

df.to_csv("quotes_dataset.csv", index=False)

print(df.head())
print("Dataset saved successfully!")
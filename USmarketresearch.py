import requests
import pandas as pd
import matplotlib.pyplot as plt

"""Fetching the US Census Bureau API data."""

API_KEY = '5882fd0192534757cc3c97f987f2028d766b8c59'
url = ("https://api.census.gov/data/2022/acs/acs1"
       "?get=NAME,B19013_001E"
       "&for=state:*"
       f"&key={API_KEY}")
response = requests.get(url)
data = response.json()

"""Converting the data into a pandas DataFrame. The first row is the column header."""

df = pd.DataFrame(data[1:], columns=data[0])
df['B19013_001E'] = pd.to_numeric(df['B19013_001E'], errors='coerce')
df = df.dropna(subset=['B19013_001E'])
df_sorted = df.sort_values(by='B19013_001E', ascending=False)
print(df_sorted[['NAME', 'B19013_001E']].head(10))
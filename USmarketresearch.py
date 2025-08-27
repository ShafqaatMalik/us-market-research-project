import requests
import pandas as pd
import matplotlib.pyplot as plt

"""Fetching the US Census Bureau API data."""

API_KEY = '5882fd0192534757cc3c97f987f2028d766b8c59'
url = ("https://api.census.gov/data/2022/acs/acs1" 
       
       "?get=NAME,B19013_001E" # B19013_001E is the median household income
       "&for=state:*" # for all states
       f"&key={API_KEY}")
response = requests.get(url)
data = response.json()

"""Converting the data into a pandas DataFrame. The first row is the column header."""

df = pd.DataFrame(data[1:], columns=data[0])
df['B19013_001E'] = pd.to_numeric(df['B19013_001E'], errors='coerce')
df = df.dropna(subset=['B19013_001E'])

"""Sorting the DataFrame by median household income and displaying the top 10 states."""

df_sorted = df.sort_values(by='B19013_001E', ascending=False)
top10 = df_sorted.head(10)
print(top10[['NAME', 'B19013_001E']].head(10))

"""Visualizing the data using a bar chart with matplotlib."""

plt.figure(figsize=(12, 6))
plt.barh(top10['NAME'], top10['B19013_001E'], color='skyblue')
plt.xlabel('State')
plt.ylabel('Median Household Income')
plt.title('Top 10  US States by Median Household Income (ACS 2022)')
plt.gca().invert_yaxis()
plt.show()   
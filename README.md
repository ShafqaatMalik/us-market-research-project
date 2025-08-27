This project uses the **US Census API** (ACS 1-Year Estimates) to identify the **Top 10 US States by Median Household Income**. It demonstrates how to work with APIs, clean and analyze data with **pandas**, and visualize insights with **matplotlib** in Python. This script fetches data from the US Census Bureau API, specifically the median household income by state for the year 2022. It processes the data using pandas and visualizes the top 10 states by median household income using a horizontal bar chart. This small project is useful for market research and product launch strategies.

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
3. **Set up API key:**
   - Register for a free API key at [US Census Bureau](https://api.census.gov/data/key_signup.html)
   - Set environment variable:
     ```bash
     export CENSUS_API_KEY="your_api_key_here"
     ```
   - Or update the `API_KEY` variable in `USmarketresearch.py`

### Sample Output

```
                NAME      B19013_001E
0             Maryland      95064
1 District of Columbia      92266
2        Massachusetts      89026
3               Hawaii      87470
4          Connecticut      83771
5           New Jersey      82545
6             New York      81386
7             Virginia      80963
8           California      80440
9           Washington      78687
```






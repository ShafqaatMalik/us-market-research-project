# US Market Research Project

A Python-based data analysis project that leverages the **US Census API** (ACS 1-Year Estimates) to identify the **Top 10 US States by Median Household Income**. This project demonstrates effective API integration, data cleaning and analysis with **pandas**, and data visualization with **matplotlib**.

## 📋 Description

This script fetches median household income data from the US Census Bureau API for all US states (2022 data) and processes it to identify market opportunities. The analysis includes data cleaning, sorting, and visualization through an intuitive horizontal bar chart. This project is particularly valuable for market research, business intelligence, and strategic planning for product launches.

## ✨ Features

- **API Integration**: Seamless connection to US Census Bureau API (ACS 1-Year Estimates)
- **Data Processing**: Robust data cleaning and transformation using pandas
- **Data Visualization**: Clear and informative horizontal bar charts using matplotlib
- **Market Insights**: Identification of top-performing states by household income
- **Business Intelligence**: Actionable data for market research and strategic planning

## 🚀 Installation

### Prerequisites
- Python 3.7 or higher
- pip package manager

### Dependencies Installation

1. Clone this repository:
```bash
git clone https://github.com/ShafqaatMalik/us-market-research-project.git
cd us-market-research-project
```

2. Install required packages:
```bash
pip install -r requirements.txt
```

## 📦 Dependencies

The project relies on the following Python packages:

- **requests**: For making HTTP requests to the Census API
- **pandas**: For data manipulation and analysis
- **matplotlib**: For creating data visualizations

## 🔑 API Configuration

This project uses the US Census Bureau API. The API key is included in the script for demonstration purposes, but for production use, consider:

- **API Endpoint**: `https://api.census.gov/data/2022/acs/acs1`
- **Data Field**: `B19013_001E` (Median Household Income)
- **Geographic Scope**: All US States (`for=state:*`)

## 💻 Usage

Run the analysis script:

```bash
python USmarketresearch.py
```

### What the Script Does:

1. **Fetches Data**: Connects to the US Census API and retrieves median household income data for all states
2. **Processes Data**: Converts JSON response to pandas DataFrame and cleans the data
3. **Analyzes Data**: Sorts states by median household income in descending order
4. **Displays Results**: Prints the top 10 states with their median household income values
5. **Visualizes Data**: Creates a horizontal bar chart showing the top 10 states

### Sample Output

The script will display a table showing:
```
                     NAME  B19013_001E
0               Maryland      91431
1      Massachusetts      89026
2           Hawaii       87722
3        Connecticut      83572
4       New Jersey      82545
...
```

And generate a horizontal bar chart titled "Top 10 US States by Median Household Income (ACS 2022)".

## 📁 Project Structure

```
us-market-research-project/
│
├── README.md                 # This file
├── USmarketresearch.py       # Main analysis script
├── requirements.txt          # Python dependencies
├── .gitignore               # Git ignore file
└── .git/                    # Git repository data
```

## 🎯 Use Cases

This project is ideal for:

- **Market Research**: Identifying high-income markets for premium products
- **Business Strategy**: Geographic expansion planning
- **Economic Analysis**: Understanding regional income distribution
- **Investment Decisions**: Targeting areas with higher purchasing power
- **Educational Purposes**: Learning API integration and data analysis

## 🔍 Data Source

- **Source**: US Census Bureau
- **Dataset**: American Community Survey (ACS) 1-Year Estimates
- **Year**: 2022
- **Geographic Level**: State
- **Indicator**: Median Household Income (B19013_001E)

## 🤝 Contributing

Contributions are welcome! Here are some ways you can contribute:

1. **Fork the repository**
2. **Create a feature branch** (`git checkout -b feature/AmazingFeature`)
3. **Commit your changes** (`git commit -m 'Add some AmazingFeature'`)
4. **Push to the branch** (`git push origin feature/AmazingFeature`)
5. **Open a Pull Request**

### Enhancement Ideas:
- Add analysis for additional income metrics
- Include county-level analysis
- Implement trend analysis across multiple years
- Add interactive visualizations
- Create export functionality for results

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 👤 Author

**Shafqaat Malik**

- GitHub: [@ShafqaatMalik](https://github.com/ShafqaatMalik)
- Project Repository: [us-market-research-project](https://github.com/ShafqaatMalik/us-market-research-project)

## 📞 Support

If you encounter any issues or have questions:

1. Check the existing [Issues](https://github.com/ShafqaatMalik/us-market-research-project/issues)
2. Create a new issue if your problem isn't already covered
3. Provide detailed information about your environment and the issue

---

**Note**: This project is for educational and research purposes. Please ensure compliance with the US Census Bureau's terms of use when using their API.
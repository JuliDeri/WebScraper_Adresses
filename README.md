# Google Search Scraper

This Python script uses the SerpAPI to perform Google searches and extract relevant data from the search results. It reads search queries from a CSV file, performs searches based on those queries, and saves the results to a new CSV file.

## Features

- Reads search queries from a CSV file.
- Uses SerpAPI to perform Google searches.
- Extracts and processes search result data including position, title, and link.
- Saves the results to a new CSV file.

## Requirements

- Python 3.x
- `serpapi` library
- `pandas` library
- `python-dotenv` library

## Installation

1. **Clone the repository:**

   git clone https://github.com/yourusername/your-repository.git
   cd your-repository

2. **Install the required Python libraries:**

    pip install -r requirements.txt
3. **Create a .env file:**

    Create a .env file in the root directory of the project with the following content:

    API_KEY=your_serpapi_key_here
    CSV_PATH=path_to_your_input_csv_file
   
Replace your_serpapi_key_here with your actual SerpAPI key and path_to_your_input_csv_file with the path to your input CSV file.

**Usage**
**1.Prepare your input CSV file:**

The input CSV file should contain search queries. The script assumes that the search queries are in the first column of the CSV file.

**2.Run the script:**

python your_script_name.py
The script will read the queries from the input CSV file, perform searches using SerpAPI, and save the results to SerpAPI_address_output_test.csv.

**Example**
If your input CSV file (serpAPI_adress_input_test.csv) contains:

query1
query2
query3

The output CSV file (SerpAPI_address_output_test.csv) will contain:


Query,Position,Title,Link
query1,1,Title1,https://example.com/link1
query2,2,Title2,https://example.com/link2
query3,3,Title3,https://example.com/link3

**License**
This project is licensed under the MIT License - see the LICENSE file for details.

**Acknowledgments**
SerpAPI for providing the search API.
pandas for data manipulation and analysis.

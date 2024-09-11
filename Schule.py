from serpapi import GoogleSearch
import csv
import pandas as pd
import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Read the API key and file path from environment variables
api_key = os.getenv("API_KEY")
csv_path = os.getenv("CSV_PATH")

# Location for Google Search
location = "Frankfurt, Hesse, Germany"

# List to store the results
results_list = []

# Read the CSV file
with open(csv_path, encoding='unicode_escape') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter='\t')

    # Loop through each row in the CSV file
    for row in csv_reader:
        query = row[0]  # Assumption: The first column contains the search queries

        # Parameters for Google Search
        params = {
            "q": query,
            "location": location,
            "hl": "de",
            "gl": "de",
            "google_domain": "google.de",
            "api_key": api_key
        }

        # Perform the search
        search = GoogleSearch(params)
        search_results = search.get_dict()

        # Process the results
        organic_results = search_results.get("organic_results", [])
        if organic_results:
            for result in organic_results:
                position = result.get("position")
                title = result.get("title")
                link = result.get("link")
                results_list.append([query, position, title, link])
        else:
            results_list.append([query, None, None, None])

# Convert results to a DataFrame
df = pd.DataFrame(results_list, columns=["Query", "Position", "Title", "Link"])

# Save DataFrame to a CSV file
output_csv_path = "SerpAPI_address_output_test.csv"
df.to_csv(output_csv_path, index=False)

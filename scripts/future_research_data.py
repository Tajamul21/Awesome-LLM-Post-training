import os
import json
import requests
import time
import pandas as pd
import matplotlib.pyplot as plt

def get_paper_count(query, year):
    """Get number of papers for a given query and year from Semantic Scholar."""
    url = f"https://api.semanticscholar.org/graph/v1/paper/search?query={query}&year={year}&limit=1&fields=year"
    headers = {'User-Agent': 'AcademicResearch/1.0 (mailto:user@example.com)'}
    
    for _ in range(10):  # Retry up to 10 times
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            data = response.json()
            return data.get('total', 0)
        elif response.status_code == 429:
            print(f"⚠️ Rate limit exceeded for {year} on query '{query}'. Retrying in 10s...")
            time.sleep(10)
        else:
            print(f"❌ Error {response.status_code} for {year} on query '{query}'")
            return 0
    return 0  # Return 0 if all retries fail

# Read CSV file with research prompts (ensure the file is CSV-formatted)
csv_path = "assets/Keywords.csv"
prompts_df = pd.read_csv(csv_path)

# Define the range of years
years = list(range(2020, 2026))  # From 2020 to 2025

# Create an output directory for saving JSON, Excel, and figure files
output_dir = "results"
os.makedirs(output_dir, exist_ok=True)

# Path for progressive JSON saving
json_path = os.path.join(output_dir, "research_trends.json")

# Dictionary to hold all results
results_dict = {}

# Process each prompt from the CSV
for index, row in prompts_df.iterrows():
    category = row['Category']
    keyword = row['Research Keyword']
    print(f"\nProcessing Keyword: '{keyword}' in Category: '{category}'")
    
    counts = []
    for year in years:
        print(f"🔍 Fetching data for {year} for keyword '{keyword}'...")
        count = get_paper_count(keyword, year)
        counts.append(count)
        time.sleep(1)  # Be polite between requests

    # Create structured data for this keyword
    data_for_keyword = [{"Year": year, "Papers Published": count} for year, count in zip(years, counts)]
    results_dict[keyword] = {
        "Category": category,
        "Data": data_for_keyword
    }
    
    # Progressively save results to JSON
    with open(json_path, "w") as json_file:
        json.dump(results_dict, json_file, indent=4)
    
    # Create a DataFrame for the current keyword and plot the results
    df_counts = pd.DataFrame(data_for_keyword)
    print(df_counts)
    
    plt.figure(figsize=(12, 6))
    bars = plt.bar(df_counts['Year'], df_counts['Papers Published'], color='#2c7fb8')
    plt.title(f'Publication Trend for "{keyword}" ({category})', fontsize=14, pad=20)
    plt.xlabel('Year', fontsize=12)
    plt.ylabel('Number of Papers', fontsize=12)
    plt.xticks(years)
    plt.grid(axis='y', linestyle='--', alpha=0.7)

    # Add value labels on top of each bar
    for bar in bars:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2., height,
                 f'{height:,}',
                 ha='center', va='bottom')
    
    plt.tight_layout()
    # Save the figure as a PNG file
    figure_filename = os.path.join(output_dir, f"Publication_Trend_{keyword.replace(' ', '_')}.png")
    plt.savefig(figure_filename)
    plt.show()

# Once all keywords have been processed, convert the JSON data into an Excel file
excel_path = os.path.join(output_dir, "research_trends.xlsx")
with pd.ExcelWriter(excel_path, engine='openpyxl') as writer:
    for keyword, info in results_dict.items():
        df = pd.DataFrame(info["Data"])
        # Excel sheet names have a maximum of 31 characters
        sheet_name = keyword[:31]
        df.to_excel(writer, sheet_name=sheet_name, index=False)

print("Process completed: JSON and Excel files have been saved.")
import requests
import json
import time
import os
from tqdm import tqdm
import pandas as pd

# Folder to store PDFs
PDF_FOLDER = "Downloaded_Papers"
os.makedirs(PDF_FOLDER, exist_ok=True)

# Dictionary to track processed papers
processed_papers = {}
max_papers = 1000  # Limit to 100 papers for efficiency
paper_count = 0
max_ref_citations = 200  # Limit references & citations per paper
rate_limit_wait = 10  # Increase wait time to 10s for API rate limits

# Function to search for papers
def search_papers(query, limit=5):
    url = f"https://api.semanticscholar.org/graph/v1/paper/search?query={query}&limit={limit}&fields=title,authors,abstract,url,tldr,year,venue,references,citations"

    for _ in range(3):  # Retry up to 3 times if 429 error occurs
        response = requests.get(url)

        if response.status_code == 200:
            return response.json().get("data", [])
        elif response.status_code == 429:
            print(f"⚠️ Rate limit exceeded. Retrying in {rate_limit_wait}s...")
            time.sleep(rate_limit_wait)
        else:
            print(f"❌ Error: {response.status_code}")
            return None
    return None  # Return None if all retries fail

# Function to fetch paper details (including references and citations)
def fetch_paper_details(paper_id, depth=1):
    """Fetches paper details with a limit on recursion depth"""
    global paper_count
    if paper_count >= max_papers:
        return None  # Stop if limit reached

    if paper_id in processed_papers:
        return processed_papers[paper_id]  # Skip duplicates

    url = f"https://api.semanticscholar.org/graph/v1/paper/{paper_id}?fields=title,authors,abstract,url,tldr,year,venue,references,citations"

    try:
        response = requests.get(url)
        if response.status_code == 429:
            print(f"⚠️ API Rate limit reached. Retrying in {rate_limit_wait}s...")
            time.sleep(rate_limit_wait)
            return fetch_paper_details(paper_id, depth)  # Retry the same call
        if response.status_code != 200:
            return None
        paper = response.json()
    except Exception:
        return None

    title = paper.get("title", "No title available")
    print(f"📄 Accessing Paper: {title}")  # Print paper title when accessing

    authors = ", ".join([author["name"] for author in paper.get("authors", [])])
    abstract = paper.get("abstract") or "No abstract available"
    tldr = paper.get("tldr", {}).get("text", "No summary available") if paper.get("tldr") else "No summary available"
    year = paper.get("year") if paper.get("year") else "Unknown Year"
    venue = paper.get("venue", "Unknown")
    link = paper.get("url", "No URL available")

    # Save references and citations details
    references = []
    citations = []

    # Limit depth to avoid long chains
    if depth <= 2:  # Allow fetching references & citations up to depth 2
        ref_ids = [ref["paperId"] for ref in paper.get("references", []) if "paperId" in ref][:max_ref_citations]
        cite_ids = [cite["paperId"] for cite in paper.get("citations", []) if "paperId" in cite][:max_ref_citations]

        for ref in tqdm(ref_ids, desc="Fetching References", leave=False):
            ref_details = fetch_paper_details(ref, depth + 1)
            if ref_details:
                references.append(ref_details)

        for cite in tqdm(cite_ids, desc="Fetching Citations", leave=False):
            cite_details = fetch_paper_details(cite, depth + 1)
            if cite_details:
                citations.append(cite_details)

    # Track processed papers
    processed_papers[paper_id] = {
        "Title": title,
        "Authors": authors,
        "Abstract": abstract,
        "TL;DR": tldr,
        "Publication Year": year,
        "Venue (Conference/Journal)": venue,
        "Link": link,
        "References": references,  # Save references
        "Citations": citations  # Save citations
    }
    paper_count += 1

    return processed_papers[paper_id]

# Query and search for papers
query = "Survey on Large Language and Reinforcement Learning"
papers = search_papers(query, limit=1)

if not papers:
    print("❌ No papers found.")
else:
    total_papers_found = len(papers)
    print(f"🔍 Found {total_papers_found} initial papers. Processing...")

    data = []
    for idx, paper in tqdm(enumerate(papers), total=len(papers), desc="Processing Papers"):
        paper_id = paper.get("paperId")
        if paper_id:
            paper_details = fetch_paper_details(paper_id)
            if paper_details:
                data.append(paper_details)

        # Save every 3 papers to avoid data loss
        if len(data) % 3 == 0:
            with open("papers_temp.json", "w", encoding="utf-8") as f:
                json.dump(data, f, indent=4)

            print(f"✅ Saved {len(data)} papers (Temporary)")

    # Save final results in JSON
    json_filename = "papers.json"
    with open(json_filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

    print(f"\n✅ **Final Report:**")
    print(f"📄 Papers Found: {total_papers_found}")
    print(f"📥 Papers Processed & Saved: {len(data)}")
    print(f"📂 PDFs Saved in: '{PDF_FOLDER}'")
    print(f"📊 Data saved to: {json_filename}")

    # Convert JSON to DataFrame and save as Excel
    df = pd.json_normalize(data)
    df.to_excel("papers.xlsx", index=False)
    print(f"📊 Data also saved to: papers.xlsx")
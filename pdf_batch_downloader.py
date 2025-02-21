import os
import sys
import requests
import logging
from urllib.parse import urljoin
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor

logging.basicConfig(filename="download_progress.log", level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

def log_progress(message):
    logging.info(message)
    print(message)

def extract_pdfs(site):
    site = site.strip()
    print(f"Extracting PDFs from: {site}")
    
    try:
        response = requests.get(site, headers=HEADERS, timeout=10)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        log_progress(f"Failed to fetch {site}: {e}")
        return []

    soup = BeautifulSoup(response.content, "html.parser")
    pdf_links = [urljoin(site, link["href"]) for link in soup.find_all("a", href=True) if link["href"].lower().endswith(".pdf")]

    log_progress(f"Found {len(pdf_links)} PDF links at {site}")
    return pdf_links

def download_pdf(url):
    filename = os.path.join("DownloadedPdfs", url.split("/")[-1])

    try:
        response = requests.get(url, headers=HEADERS, timeout=15)
        response.raise_for_status()

        with open(filename, "wb") as file:
            file.write(response.content)

        log_progress(f"Downloaded: {filename} ({len(response.content)} bytes)")
    except requests.exceptions.RequestException as e:
        log_progress(f"Failed to download {url}: {e}")

def main(sites):
    os.makedirs("DownloadedPdfs", exist_ok=True)

    all_pdf_links = []
    for site in sites:
        all_pdf_links.extend(extract_pdfs(site))

    if not all_pdf_links:
        log_progress("No PDFs found. Exiting.")
        return

    with ThreadPoolExecutor(max_workers=4) as executor:
        executor.map(download_pdf, all_pdf_links)

if __name__ == "__main__":
    sites = sys.argv[1:] if len(sys.argv) > 1 else input("Enter URLs (comma-separated): ").split(",")
    main(sites)

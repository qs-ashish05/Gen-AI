from duckduckgo_search import DDGS
from bs4 import BeautifulSoup
import requests

def clean_text_from_url(url):
    try:
        headers = {
            "User-Agent": "Mozilla/5.0"
        }
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, 'html.parser')

        # Remove unwanted elements
        for tag in soup(['script', 'style', 'noscript', 'header', 'footer', 'form', 'svg', 'nav', 'aside']):
            tag.decompose()
        
        # Extract paragraph text
        paragraphs = soup.find_all('p')
        text = "\n".join(p.get_text(strip=True) for p in paragraphs if p.get_text(strip=True))
        
        return text
    except Exception as e:
        return f"[Failed to fetch from {url}]: {str(e)}"


def get_combined_text(query, num_results=5):
    all_text = ""
    ddgs = DDGS()
    results = ddgs.text(query, max_results=num_results)
    
    for res in results:
        url = res.get("href")
        if url:
            print(f"Scraping: {url}")
            cleaned = clean_text_from_url(url)
            all_text += f"\n\n--- Content from {url} ---\n\n{cleaned}"
    
    return all_text


if __name__ == "__main__":
    query = "What is the current status of the Build Back Better Act?"
    combined_text = get_combined_text(query)
    
    # Optional: Save to a file or just print
    print(combined_text[:3000])  # Print first 3000 chars

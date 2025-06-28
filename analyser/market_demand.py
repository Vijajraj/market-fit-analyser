import requests
from bs4 import BeautifulSoup

def get_trending_keywords(product):
    url = f"https://www.google.com/search?q={product}&tbm=nws"
    headers = {"User-Agent": "Mozilla/5.0"}
    page = requests.get(url, headers=headers)
    soup = BeautifulSoup(page.content, "html.parser")
    headlines = soup.find_all("h3")
    keywords = [headline.text for headline in headlines]
    return keywords[:5]  # Return top 5 headlines

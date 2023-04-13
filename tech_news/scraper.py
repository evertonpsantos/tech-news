import requests
import time
from bs4 import BeautifulSoup


# Requisito 1
def fetch(url):
    try:
        time.sleep(1)
        response = requests.get(
            url, headers={"user-agent": "Fake user-agent"}, timeout=3
        )
        if response.status_code != 200:
            return None
        return response.text
    except requests.ReadTimeout:
        return None


# Requisito 2
def scrape_updates(html_content):
    news_soup = BeautifulSoup(html_content, "html.parser")
    h2_tags = news_soup.find_all("h2", {"class": "entry-title"})
    a_tags = []
    for h2 in h2_tags:
        a_tags.append(h2.a["href"])
    if len(a_tags) == 0:
        return []
    return a_tags


# Requisito 3
def scrape_next_page_link(html_content):
    news_soup = BeautifulSoup(html_content, "html.parser")
    try:
        return news_soup.find("a", {"class": "next page-numbers"})["href"]
    except TypeError:
        return None


# Requisito 4
def scrape_news(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""

from tech_news.database import create_news
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
    news_soup = BeautifulSoup(html_content, "html.parser")
    return {
        "url": news_soup.find("link", {"rel": "canonical"})["href"],
        "title": news_soup.find("h1", {"class": "entry-title"}).string.strip(),
        "timestamp": news_soup.find("li", {"class": "meta-date"}).string,
        "writer": news_soup.find("a", {"class": "url fn n"}).string,
        "reading_time": int(
            news_soup.find("li", {"class": "meta-reading-time"})
            .text[:2]
            .strip()
        ),
        "summary": news_soup.find(
            "div", {"class": "entry-content"}
        ).p.getText().strip(),
        "category": news_soup.find("span", {"class": "label"}).string,
    }


# Requisito 5
def get_tech_news(amount):
    urls = []
    scraped_news = []
    url_to_scrape = "https://blog.betrybe.com/"

    while amount > len(urls):
        page_content = fetch(url_to_scrape)
        urls.extend(scrape_updates(page_content))

        url_to_scrape = scrape_next_page_link(page_content)

    for url in urls:
        current_news = fetch(url)

        if len(scraped_news) < amount:
            scraped_news.append(scrape_news(current_news))

    create_news(scraped_news)
    return scraped_news

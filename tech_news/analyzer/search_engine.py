from tech_news.database import search_news
import re


# Requisito 7
def search_by_title(title):
    compiled_regex = re.compile(rf'{title}', re.I)
    found_results = search_news({"title": {"$regex": compiled_regex}})
    return [(result["title"], result["url"]) for result in found_results]


# Requisito 8
def search_by_date(date):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""

from tech_news.database import search_news
import re
from datetime import datetime


# Requisito 7
def search_by_title(title):
    compiled_regex = re.compile(rf"{title}", re.I)
    found_results = search_news({"title": {"$regex": compiled_regex}})
    return [(result["title"], result["url"]) for result in found_results]


# Requisito 8
def search_by_date(date):
    try:
        converted_date = datetime.strptime(date, "%Y-%m-%d").strftime(
            "%d/%m/%Y"
        )
        found_results = search_news({"timestamp": {"$regex": converted_date}})
        return [(result["title"], result["url"]) for result in found_results]
    except ValueError:
        raise ValueError("Data inválida")


# Requisito 9
def search_by_category(category):
    compiled_regex = re.compile(rf'{category}', re.I)
    found_results = search_news({"category": {"$regex": compiled_regex}})
    return [(result["title"], result["url"]) for result in found_results]

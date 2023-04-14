from tech_news.database import search_news
from datetime import datetime


# Requisito 7
def search_by_title(title):
    found_results = search_news({"title": {"$regex": title, "$options": "i"}})
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
    found_results = search_news(
        {"category": {"$regex": category, "$options": "i"}}
    )
    return [(result["title"], result["url"]) for result in found_results]

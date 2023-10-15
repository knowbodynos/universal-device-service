import os

from serpapi import GoogleSearch


def get_search_keywords(img_url):
    search = GoogleSearch(
        {"api_key": os.getenv("SERP_API_KEY"), "engine": "google_lens", "url": img_url}
    )
    results = search.get_dict()
    keywords = [x["title"] for x in results["knowledge_graph"]]
    return keywords

from bs4 import BeautifulSoup
from typing import Dict, List

from web_scrapper import WebScraper


class DataExtractor:
    def __init__(self, url: str):
        self.scraper = WebScraper(url)

    def organize_adjectives(self) -> Dict[str, List[str]]:
        data: Dict[str, List[str]] = {}
        animals_data = self.scraper.extract_animal_data()
        for animal in animals_data:
            for adj in animal.adjectives:
                if adj not in data:
                    data[adj] = []
                data[adj].append(animal.name)
        return data









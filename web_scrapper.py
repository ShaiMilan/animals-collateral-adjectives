from concurrent.futures import ThreadPoolExecutor

import requests
from bs4 import BeautifulSoup
from typing import Optional, List, Tuple

from model import AnimalData


class WebScraper:
    def __init__(self, url: str):
        self.url: str = url
        self._soup: Optional[BeautifulSoup] = None
        self.fetch_data()

    def fetch_data(self) -> None:
        try:
            response = requests.get(self.url)
            response.raise_for_status()  # Raises an HTTPError for bad responses
            self._soup = BeautifulSoup(response.text, 'html.parser')
        except requests.RequestException as e:
            print(f"Error fetching data: {e}")
            self._soup = None

    def extract_animal_data(self) -> List[AnimalData]:
        animal_list: List[AnimalData] = list()
        if self._soup:
            tables = self._soup.find_all('table', class_='wikitable sortable')
            for table in tables:
                self.extract_table_data(animal_list, table)
        return animal_list

    def extract_table_data(self, animal_list, table):
        headers = [header.text.strip() for header in table.find('tr').find_all('th')]
        name_idx = 0
        adjective_idx = headers.index('Collateral adjective')
        rows = table.find_all('tr')[1:]  # Skip header row

        # Process each row in a separate thread
        with ThreadPoolExecutor() as executor:
            futures = [executor.submit(self.process_row, animal_list, row, name_idx, adjective_idx) for row in rows]
            for future in futures:
                future.result()  # Ensure all threads complete

    def process_row(self, animal_list, row, name_idx, adjective_idx):
        cells = row.find_all('td')
        if len(cells) > max(name_idx, adjective_idx):  # Ensure there are enough columns
            animal = cells[name_idx].text.strip()
            adjectives = cells[adjective_idx].get_text(separator=', ', strip=True).split(', ')
            animal_list.append(AnimalData(name=animal, adjectives=adjectives))


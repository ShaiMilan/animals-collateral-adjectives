import os
import requests
from bs4 import BeautifulSoup
from typing import List
from concurrent.futures import ThreadPoolExecutor


class ImageDownloader:
    def __init__(self, animals: List[str]):
        self.animals: List[str] = animals
        self.base_url: str = "https://en.wikipedia.org/wiki/"
        self.image_folder: str = "animal_images"

    def download_images(self) -> None:
        if not os.path.exists(self.image_folder):
            os.makedirs(self.image_folder)

        with ThreadPoolExecutor() as executor:
            executor.map(self.download_and_save_image, self.animals)

    def download_and_save_image(self, animal: str) -> None:
        try:
            page_url = self.base_url + animal.replace(" ", "_")
            print(f"Getting image from {page_url}")
            page_response = requests.get(page_url)
            page_soup = BeautifulSoup(page_response.text, 'html.parser')
            infobox = page_soup.find('table', class_='infobox') or page_soup.find('div', class_='thumbimage') \
                      or page_soup.find('figure', class_='mw-default-size')
            if infobox:
                image_tag = infobox.find('img')
                if image_tag:
                    image_url = "https:" + image_tag['src']
                    image_response = requests.get(image_url)
                    if image_response.status_code == 200:
                        with open(os.path.join(self.image_folder, f"{animal.replace('/', '_')}.jpg"), 'wb') as f:
                            f.write(image_response.content)
        except Exception as e:
            print(f"Failed to download image for {animal}: {e}")


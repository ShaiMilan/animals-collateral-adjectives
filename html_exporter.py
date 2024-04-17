import os
from typing import Dict, List

from loguru import logger


class HTMLExporter:
    def __init__(self, data: Dict[str, List[str]], image_folder: str):
        self.data: Dict[str, List[str]] = data
        self.image_folder: str = image_folder
        self.html_path: str = "animal_adjectives.html"

    def export_to_html(self) -> None:
        logger.info(f"Exporting animals data to {self.html_path}")
        with open(self.html_path, 'w') as file:
            file.write("<html><body><h1>Animal Adjectives</h1>")
            for adjective, animals in self.data.items():
                file.write(f"<h2>{adjective}</h2><ul>")
                for animal in animals:
                    img_path = os.path.join(self.image_folder, animal + ".jpg")
                    if os.path.exists(img_path):
                        file.write(f"<li>{animal} <img src='{img_path}' alt='{animal}'/></li>")
                    else:
                        file.write(f"<li>{animal}</li>")
                file.write("</ul>")
            file.write("</body></html>")
        logger.info(f"Exported")

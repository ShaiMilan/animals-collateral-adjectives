import os
from typing import Dict, List


class HTMLExporter:
    def __init__(self, data: Dict[str, List[str]], image_folder: str):
        self.data: Dict[str, List[str]] = data
        self.image_folder: str = image_folder
        self.html_path: str = "animal_adjectives.html"

    def export_to_html(self) -> None:
        with open(self.html_path, 'w') as file:
            file.write("<html><body><h1>Animal Adjectives</h1>")
            for adjective, animals in self.data.items():
                file.write(f"<h2>{adjective}</h2><ul>")
                for animal in animals:
                    img_path = os.path.join(self.image_folder, animal + ".jpg")
                    file.write(f"<li>{animal} <img src='{img_path}' alt='{animal}'/></li>")
                file.write("</ul>")
            file.write("</body></html>")

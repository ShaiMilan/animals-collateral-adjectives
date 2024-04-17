from data_extractor import DataExtractor
from html_exporter import HTMLExporter
from image_downloader import ImageDownloader
from output_manager import OutputManager


def main() -> None:
    url = 'https://en.wikipedia.org/wiki/List_of_animal_names'
    extractor = DataExtractor(url)
    adjectives = extractor.organize_adjectives()

    # Image downloading
    all_animals = set([animal for animals in adjectives.values() for animal in animals])
    downloader = ImageDownloader(list(all_animals))
    downloader.download_images()

    # HTML output
    html_exporter = HTMLExporter(adjectives, "animal_images")
    html_exporter.export_to_html()

    output = OutputManager(adjectives)
    output.display_data()


if __name__ == '__main__':
    main()

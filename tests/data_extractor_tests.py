import unittest
from unittest.mock import patch, MagicMock

import requests

from data_extractor import DataExtractor
from web_scrapper import WebScraper
from model import AnimalData


class TestDataExtractor(unittest.TestCase):
    @patch("web_scrapper.WebScraper.fetch_data")
    def setUp(self, fetch_data_mock):
        self.mock_scraper = MagicMock(spec=WebScraper)
        self.data_extractor = DataExtractor(url="https://fakeurl.com")
        self.data_extractor.scraper = self.mock_scraper

    def test_organize_adjectives_empty(self):
        # Test with no animals
        self.mock_scraper.extract_animal_data.return_value = []
        result = self.data_extractor.organize_adjectives()
        self.assertEqual(result, {}, "Should return an empty dictionary for no animals")

    def test_organize_adjectives_single_animal(self):
        # Test with one animal having one adjective
        self.mock_scraper.extract_animal_data.return_value = [
            AnimalData(name="Lion", adjectives=["Feline"])
        ]
        result = self.data_extractor.organize_adjectives()
        expected = {"Feline": ["Lion"]}
        self.assertEqual(result, expected, "Should map 'Feline' to ['Lion']")

    def test_organize_adjectives_multiple_animals(self):
        # Test with multiple animals and shared adjectives
        self.mock_scraper.extract_animal_data.return_value = [
            AnimalData(name="Lion", adjectives=["Feline"]),
            AnimalData(name="Tiger", adjectives=["Feline"])
        ]
        result = self.data_extractor.organize_adjectives()
        expected = {"Feline": ["Lion", "Tiger"]}
        self.assertEqual(result, expected, "Should map 'Feline' to ['Lion', 'Tiger']")

    @patch("web_scrapper.WebScraper.fetch_data")
    def test_http_error_handling(self, fetch_data_mock):
        fetch_data_mock.side_effect = requests.RequestException("Server Error")

        with self.assertRaises(requests.RequestException):
            DataExtractor(url="https://fakeurl.com")


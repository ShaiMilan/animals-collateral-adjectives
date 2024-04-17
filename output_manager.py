from typing import Dict, List

from loguru import logger


class OutputManager:
    def __init__(self, data: Dict[str, List[str]]):
        self.data: Dict[str, List[str]] = data

    def display_data(self) -> None:
        logger.info("Fetched animals adjective data")
        for adjective, animals in self.data.items():
            logger.info(f"{adjective}: {', '.join(animals)}")

from typing import Dict, List


class OutputManager:
    def __init__(self, data: Dict[str, List[str]]):
        self.data: Dict[str, List[str]] = data

    def display_data(self) -> None:
        for adjective, animals in self.data.items():
            print(f"{adjective}: {', '.join(animals)}")

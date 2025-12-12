from abc import ABC, abstractmethod

# Abstract class. Defines the interface for all scrapers
class BaseScraper(ABC):
    def __init__(self, url: str):
        self.url = url

    @abstractmethod
    def extract_price(self) -> float:
        pass

    @abstractmethod
    def extract_name(self) -> str:
        pass
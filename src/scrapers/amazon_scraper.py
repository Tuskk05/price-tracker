import requests
from bs4 import BeautifulSoup
from src.scrapers.base_scraper import BaseScraper
import random
import time

class AmazonScraper(BaseScraper):

    def __init__(self, url: str):
        super().__init__(url)
        self.soup = None  # Clears cache to save the HTML

    #Fetches page content
    def _get_soup(self):
        if self.soup:
            return self.soup

        # Different user-agents
        user_agents = [
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/115.0"
        ]
        
        headers = {
            "User-Agent": random.choice(user_agents),
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
            "Accept-Language": "es-ES,es;q=0.9,en;q=0.8",
            "Connection": "keep-alive",
            "Upgrade-Insecure-Requests": "1",
            "Sec-Fetch-Dest": "document",
            "Sec-Fetch-Mode": "navigate",
            "Sec-Fetch-Site": "none",
            "DNT": "1", 
        }
        
        try:
            # Seleep to simulate human behaviour
            time.sleep(random.uniform(1, 2))
            
            response = requests.get(self.url, headers=headers, timeout=15)
            response.raise_for_status()
            
            self.soup = BeautifulSoup(response.content, "html.parser")
            return self.soup
            
        except requests.RequestException as e:
            print(f"Error fetching URL {self.url}: {e}")
            return None

    def extract_price(self) -> float:
        soup = self._get_soup()
        if not soup:
            return 0.0

        price_selectors = [
            "span.a-price span.a-offscreen",
            "span.a-price-whole",
            "#priceblock_ourprice",
            ".apexPriceToPay span.a-offscreen"
        ]

        for selector in price_selectors:
            element = soup.select_one(selector)
            if element:
                price_text = element.get_text().strip()
                clean_price = (
                    price_text.replace("€", "")
                              .replace("$", "")
                              .replace("\xa0", "")
                              .strip()
                )
                # Replace american to european notation
                clean_price = clean_price.replace(".", "").replace(",", ".")
                
                try:
                    return float(clean_price)
                except ValueError:
                    continue
        return 0.0

    def extract_name(self) -> str:
        soup = self._get_soup()
        if not soup:
            return "Unknown Product"

        title_selectors = ["#productTitle", "#title", "h1.a-size-large"]
        
        for selector in title_selectors:
            element = soup.select_one(selector)
            if element:
                return element.get_text().strip()
        
        if soup.select_one("form[action*='/errors/validateCaptcha']"):
            return "BLOCKED: CAPTCHA DETECTED"
            
        return "Unknown Product"
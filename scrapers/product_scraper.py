import requests
from bs4 import BeautifulSoup


class ProductScraper:
    def __init__(self, url, item_name):
        self.url = url
        self.item_name = item_name

    def fetch_page(self):
        try:
            response = requests.get(self.url)
            response.raise_for_status()
            return response.text
        except requests.RequestException as e:
            print(f"Failed to fetch the webpage: {e}")
            return None

    def check_availability(self):
        page_content = self.fetch_page()
        if page_content:
            soup = BeautifulSoup(page_content, 'html.parser')
            item_links = soup.find_all('a', string=lambda x: x and self.item_name in x)

            for link in item_links:
                print(f"Found link: {link.get('href')} with text: {link.get_text()}")

            return len(item_links) > 0
        return False

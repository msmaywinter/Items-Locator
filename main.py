from scrapers.product_scraper import ProductScraper
from notifications.send_email import EmailNotifier


def main():
    url = 'https://tzilzul.co.il/product-category/%d7%98%d7%9c%d7%a4%d7%95%d7%a0%d7%99%d7%9d-%d7%a1%d7%9c%d7%95%d7%9c%d7%a8%d7%99%d7%99%d7%9d/prod_cat-google-pixel/'
    item_name = 'Google Pixel 8a'

    scraper = ProductScraper(url, item_name)
    notifier = EmailNotifier()

    if scraper.check_availability():
        subject = f'{item_name} is now available!'
        body = f'The {item_name} is now available in the store. Check it out: {url}'
        notifier.send_notification(subject, body)
    else:
        print("Product not available")


if __name__ == '__main__':
    main()

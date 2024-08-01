# Items Locator

This project is a web scraper that monitors a specific webpage for new items and sends an email notification when a new item is found. The example use case is monitoring a smartphone store's webpage to find when a specific model (e.g., Google Pixel 8a) becomes available.

## Features

- Scrapes a specified webpage to check for the availability of a specific item.
- Sends an email notification when the item is found.
- Configurable to monitor different webpages and items.

## Setup

1. **Clone the Repository and Setup Environment:**

   ```bash
   git clone https://github.com/yourusername/itemsLocator.git
   cd itemsLocator

   # Create and Activate Virtual Environment
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`

   # Install Dependencies
   pip install -r requirements.txt

   # Configure Environment Variables
   echo "EMAIL_USER=your_email@gmail.com" > .env
   echo "EMAIL_PASS=your_email_password" >> .env
   echo "RECEIVER_EMAIL=receiver_email@example.com" >> .env

   # Usage
   python html_scrapper.py

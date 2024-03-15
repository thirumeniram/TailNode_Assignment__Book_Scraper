# index.py
from model.book import initialize_db
from controller.scrape_controller import scrape_and_store_books

def main():
    initialize_db()  # Initialize the database and create table if not exists
    scrape_and_store_books()  # Scrape and store books data

if __name__ == '__main__':
    main()

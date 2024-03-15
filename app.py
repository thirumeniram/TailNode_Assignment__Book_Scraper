# index.py
from model.book import initialize_db
from controller.scrape_controller import scrape_and_store_books

def main():
    initialize_db()  # Initializing the database and create table if not exists
    scrape_and_store_books()  # Scraping and storing books data

if __name__=='__main__':
    main()

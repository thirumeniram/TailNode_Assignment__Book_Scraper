# controller/scrape_controller.py
import requests
from bs4 import BeautifulSoup
from psycopg2.extras import execute_values
from model.book import get_connection

BASE_URL = "http://books.toscrape.com/catalogue/page-{}.html"

def scrape_books_from_page(page_index):
    url = BASE_URL.format(page_index)
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    books = []

    for book in soup.select('.product_pod'):
        title = book.select_one('h3 a')['title']
        price = book.select_one('.product_price .price_color').text
        availability = book.select_one('.product_price .availability').text.strip()
        rating = book.select_one('p')['class'][1]
        books.append((title, price, availability, rating))

    return books

def insert_books(books):
    conn = get_connection()
    cur = conn.cursor()
    query = "INSERT INTO books1 (title, price, availability, rating) VALUES %s;"
    execute_values(cur, query, books)
    conn.commit()
    conn.close()

def scrape_and_store_books():
    all_books = []
    print("Scraping and insertion process started.")
    for page_index in range(1, 51):
        books_from_page = scrape_books_from_page(page_index)
        if books_from_page:
            insert_books(books_from_page)
            all_books.extend(books_from_page)
        else:
            break
    print("Scraping and insertion process completed.")
    return all_books

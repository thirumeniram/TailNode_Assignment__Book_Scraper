# P Book Data Scraper

This project is designed to scrape book data from [Books to Scrape](http://books.toscrape.com) across all 50 pages of the website. It extracts book attributes such as name, price, availability, and ratings, and then stores this data in a postgres database. 

## Functional Requirements Implemented

- Scraped book attributes: name, price, availability, and ratings from the website.
- Stored the scraped data in a postgres database.

## Installation

Follow these steps to set up and run the project:

1. **Clone the Repository**
   
    Clone the project to your local machine:https://github.com/thirumeniram/TailNode_Assignment__Book_Scraper.git
  
2. cd TailNode_Assignment_part_A_User_DataColleto

3. Create and activate a virtual environment:
   - For Windows:
     - python -m venv venv
     - \venv\Scripts\activate
       
   - For macOS/Linux:
     - python3 -m venv venv
     - source venv/bin/activate
       
4. Install Dependencies
    - pip install -r requirements.txt
   
5. Run the application
    - python app.py

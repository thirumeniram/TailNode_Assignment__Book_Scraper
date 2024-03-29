import psycopg2
from config.postgres import DATABASE_URL

#connecting to the PostgreSQL database using the connection string defined in DATABASE_URL.
def get_connection():
    return psycopg2.connect(DATABASE_URL)

#Initializes the database by creating a new table for storing books.
def initialize_db():
    conn=get_connection()
    cur=conn.cursor()
    create_table_query = """
    CREATE TABLE IF NOT EXISTS books1 (
        id SERIAL PRIMARY KEY,
        title VARCHAR(255),
        price VARCHAR(50),
        availability VARCHAR(50),
        rating VARCHAR(50)
    );
    """
    cur.execute(create_table_query)
    conn.commit()
    print("Table creation completed.")
    conn.close()

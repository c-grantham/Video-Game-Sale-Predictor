import pandas as pd
from sqlalchemy import create_engine
from pricehistory import get_price_history
from searchgames import get_titles
# create_engine is a function that opens a connection to a SQL DB

# Login credential connection strings to Docker PostgreSQL
DB_USER = 'gp_user'
DB_PASS = 'gp_pass'
DB_HOST = 'localhost'
DB_PORT = '5432'
DB_NAME = 'gamepriceiq'

# Format SQLAlchemy connection to database url
DATABASE_URL = f"postgresql+psycopg2://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

def load_data(pricing):
    try:
        # Create a connection to the database
        engine = create_engine(DATABASE_URL)
        # Open a safe connection inside a transaction
        with engine.begin() as conn:
            # Take this DataFrame and write it into a SQL table
            pricing.to_sql("pricehistory", conn, if_exists="replace", index=True)
            print("Data written to PostgreSQL.")
    except Exception as e:
        print("Failed to connect to the database or write data.")
        print(e)
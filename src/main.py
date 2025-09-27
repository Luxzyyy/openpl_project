from extract import get_openpowerlifting_data
from load import load_data_to_supabase
from sqlalchemy import create_engine
from dotenv import load_dotenv
import pandas as pd
import os

# Load environment variables from .env
load_dotenv()

# Fetch variables
USER = os.getenv("user")
PASSWORD = os.getenv("password")
HOST = os.getenv("host")
PORT = os.getenv("port")
DBNAME = os.getenv("dbname")

# Construct the SQLAlchemy connection string
DATABASE_URL = f"postgresql+psycopg2://{USER}:{PASSWORD}@{HOST}:{PORT}/{DBNAME}?sslmode=require"

# Create the SQLAlchemy engine
engine = create_engine(DATABASE_URL)

# Test the connection
try:
    with engine.connect() as connection:
        print("Connection successful!")

except Exception as e:
    print(f"Failed to connect: {e}")


# Upload data in chunks
chunk_iter = get_openpowerlifting_data()

print(next(chunk_iter).head())  # Print the first few rows of the first chunk to verify

for i, chunk in enumerate(chunk_iter):
    print(f"Loading chunk {i+1}")
    load_data_to_supabase(chunk, "openpl", engine)


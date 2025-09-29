import os
import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv
from extract import get_openpowerlifting_data
from load import load_data_to_supabase


def main():
    # Load environment variables from .env file
    load_dotenv(dotenv_path="/opt/airflow/.env")

    # Fetch and validate env vars
    USER = os.getenv("SUPABASE_DB_USER")
    PASSWORD = os.getenv("SUPABASE_DB_PASSWORD")
    HOST = os.getenv("SUPABASE_DB_HOST")
    PORT = os.getenv("SUPABASE_DB_PORT", "5432")
    DBNAME = os.getenv("SUPABASE_DB_NAME")

    if not all([USER, PASSWORD, HOST, PORT, DBNAME]):
        raise EnvironmentError("Missing one or more required environment variables.")

    # SQLAlchemy connection string
    DATABASE_URL = f"postgresql+psycopg2://{USER}:{PASSWORD}@{HOST}:{PORT}/{DBNAME}?sslmode=require"

    # Create engine
    engine = create_engine(DATABASE_URL)

    # Test DB connection
    try:
        with engine.connect() as conn:
            print("✅ Connected to Supabase PostgreSQL")
    except Exception as e:
        print(f"❌ Failed to connect to DB: {e}")
        return

    # Load CSV data in chunks
    chunk_iter = get_openpowerlifting_data()

    for i, chunk in enumerate(chunk_iter, 1):
        print(f"🔄 Loading chunk {i}...")
        load_data_to_supabase(chunk, "openpl", engine)

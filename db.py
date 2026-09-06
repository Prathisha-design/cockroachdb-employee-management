import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()


def get_connection():
    database_url = os.getenv("DATABASE_URL")

    if not database_url:
        raise ValueError("DATABASE_URL is missing from .env")

    return psycopg2.connect(database_url)


if __name__ == "__main__":
    try:
        conn = get_connection()

        with conn.cursor() as cursor:
            cursor.execute("SELECT version();")
            version = cursor.fetchone()[0]

        print("Connected to CockroachDB successfully!")
        print("Database version:", version)

        conn.close()

    except Exception as e:
        print("Connection failed!")
        print(e)
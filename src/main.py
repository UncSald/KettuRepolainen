import psycopg2
from os import getenv
from dotenv import load_dotenv

load_dotenv()

def main():

    database_url = getenv("DATABASE_URL")
    
    conn = psycopg2.connect(database_url, sslmode='require')
    cur = conn.cursor()

    cur.execute('SELECT VERSION()')
    version = cur.fetchone()[0]
    print(f"Database version: {version}")

    cur.close()
    conn.close()

if __name__ == "__main__":
    main()

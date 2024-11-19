import psycopg2
from os import getenv
from dotenv import load_dotenv
load_dotenv()


def main():
    conn = psycopg2.connect(getenv("DB_KEY"))

    query_sql = 'SELECT VERSION()'

    cur = conn.cursor()
    cur.execute(query_sql)

    version = cur.fetchone()[0]
    print(version)


if __name__ == "__main__":
    main()
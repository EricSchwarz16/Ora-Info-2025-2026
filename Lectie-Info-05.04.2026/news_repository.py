import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()

def get_connection():
    return psycopg2.connect(
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT"),
        dbname=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD")
    )

class NewsRepository:
    def get_by_id(self, news_id):
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT * FROM news WHERE id = %s", (news_id,))
                return cur.fetchone()

    def get_all(self):
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT * FROM news")
                return cur.fetchall()

    def get_top_k(self, k, timeframe_days):
        query = """
            SELECT n.*, COUNT(v.id) as total_views
            FROM news n
            LEFT JOIN views v ON n.id = v.news_id
            WHERE v.date >= CURRENT_DATE - MAKE_INTERVAL(days => %s)
            GROUP BY n.id
            ORDER BY total_views DESC
            LIMIT %s
        """
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(query, (timeframe_days, k))
                return cur.fetchall()

    def add(self, title, description, content, photo):
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    "INSERT INTO news (title, description, content, photo) VALUES (%s, %s, %s, %s) RETURNING id",
                    (title, description, content, photo)
                )
                return cur.fetchone()[0]

    def increment_views(self, news_id, date):
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute("INSERT INTO views (date, news_id) VALUES (%s, %s)", (date, news_id))
                conn.commit()

    def get_all_ids(self):
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT id FROM news")
                return [row[0] for row in cur.fetchall()]

import os
import psycopg2
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

def get_connection():
    return psycopg2.connect(
        host = os.getenv("DB_HOST"),
        port =os.getenv("DB_PORT"),
        dbname = os.getenv("DB_NAME"),
        user = os.getenv("DB_USER"),
        password = os.getenv("DB_PASSWORD")
    )

class VideoRepository:
    def get_by_id(self, video_id):
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT * FROM videos WHERE id = %s", (video_id,))
                return cur.fetchone()
    
    def get_views_by_id(self, id):
        query = """
            SELECT v.*, COUNT(v.id) as total_views
            FROM videos v
            LEFT JOIN views vi on v.id = vi.videos_id
            WHERE v.id = %s
            GROUP BY v.id
        """
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(query, (id,))
                return cur.fetchall()
    
    def get_all(self):
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT * FROM videos")
                return cur.fetchall()
    
    def get_top_k(self, k, timeframe_days):
        query = """
            SELECT v.*, COUNT(vi.id) as total_views
            FROM videos v
            LEFT JOIN views vi on v.id = vi.videos_id
            WHERE vi.date >= CURRENT_DATE - MAKE_INTERVAL(days => %s)
            GROUP BY v.id
            ORDER BY total_views DESC
            LIMIT %s
            """
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(query, (timeframe_days, k))
                return cur.fetchall()
    
    def add(self, title, date, author, content, URL):
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute("INSERT INTO videos (title, date, author, content, URL) VALUES (%s, %s, %s, %s, %s) RETURNING id",
                (title, date, author, content, URL))
                return cur.fetchone()[0]
    
    def increment_views(self, video_id, date):
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute("INSERT INTO views (date, videos_id) VALUES (%s, %s)", (date, video_id))
                conn.commit()
    
    def get_all_ids(self):
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT id FROM videos")
                return [row[0] for row in cur.fetchall()]

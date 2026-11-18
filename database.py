
import sqlite3
from pathlib import Path
from datetime import datetime

BASE_DIR = Path(__file__).parent
DATABASE_PATH = BASE_DIR / "database" / "civictrack.db"


def get_connection():
    DATABASE_PATH.parent.mkdir(parents=True, exist_ok=True)

    connection = sqlite3.connect(DATABASE_PATH)
    connection.row_factory = sqlite3.Row

    return connection


def initialize_database():
    with get_connection() as connection:

        connection.execute("""
            CREATE TABLE IF NOT EXISTS complaints (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                complaint_id TEXT UNIQUE,
                name TEXT NOT NULL,
                phone TEXT,
                category TEXT NOT NULL,
                location TEXT NOT NULL,
                description TEXT NOT NULL,
                severity INTEGER NOT NULL,
                people_affected INTEGER NOT NULL,
                safety_impact INTEGER NOT NULL,
                priority TEXT NOT NULL,
                priority_score INTEGER NOT NULL,
                status TEXT DEFAULT 'Pending',
                created_at TEXT NOT NULL,
                updated_at TEXT NOT NULL
            )
        """)


def generate_complaint_id():
    with get_connection() as connection:
        cursor = connection.execute(
            "SELECT COUNT(*) FROM complaints"
        )
        count = cursor.fetchone()[0] + 1

    return f"CIVIC-{datetime.now():%Y%m%d}-{count:04d}"


def add_complaint(data):
    complaint_id = generate_complaint_id()
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with get_connection() as connection:
        connection.execute("""
            INSERT INTO complaints (
                complaint_id, name, phone, category, location,
                description, severity, people_affected,
                safety_impact, priority, priority_score,
                status, created_at, updated_at
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            complaint_id,
            data["name"],
            data["phone"],
            data["category"],
            data["location"],
            data["description"],
            data["severity"],
            data["people_affected"],
            data["safety_impact"],
            data["priority"],
            data["priority_score"],
            "Pending",
            current_time,
            current_time
        ))

    return complaint_id


def get_all_complaints():
    with get_connection() as connection:
        cursor = connection.execute("""
            SELECT * FROM complaints
            ORDER BY created_at DESC
        """)
        return [dict(row) for row in cursor.fetchall()]


def get_complaint(complaint_id):
    with get_connection() as connection:
        cursor = connection.execute("""
            SELECT * FROM complaints
            WHERE complaint_id = ?
        """, (complaint_id,))

        row = cursor.fetchone()
        return dict(row) if row else None


def update_complaint_status(complaint_id, status):
    with get_connection() as connection:
        cursor = connection.execute("""
            UPDATE complaints
            SET status = ?, updated_at = ?
            WHERE complaint_id = ?
        """, (
            status,
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            complaint_id
        ))

        return cursor.rowcount > 0


def delete_complaint(complaint_id):
    with get_connection() as connection:
        cursor = connection.execute("""
            DELETE FROM complaints
            WHERE complaint_id = ?
        """, (complaint_id,))

        return cursor.rowcount > 0

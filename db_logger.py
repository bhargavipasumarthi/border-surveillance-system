import sqlite3
from datetime import datetime

def log_event(object_id, event):

    conn = sqlite3.connect("events.db")
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO events (
        timestamp,
        object_id,
        event
    )
    VALUES (?, ?, ?)
    """, (
        datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        object_id,
        event
    ))

    conn.commit()
    conn.close()
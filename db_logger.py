import sqlite3
from datetime import datetime

def log_event(object_id, event, threat_level):
    object_id = int(object_id)

    conn = sqlite3.connect("events.db")
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO events (
        timestamp,
        object_id,
        event,
        threat_level
    )
    VALUES (?, ?, ?, ?)
    """, (
        datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        object_id,
        event,
        threat_level
    ))

    conn.commit()
    conn.close()
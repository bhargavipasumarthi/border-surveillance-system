import sqlite3
from datetime import datetime

conn = sqlite3.connect("events.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS events (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    timestamp TEXT,
    object_id INTEGER,
    event TEXT
)
""")

cursor.execute("""
INSERT INTO events (timestamp, object_id, event)
VALUES (?, ?, ?)
""", (
    datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    1,
    "Entered Restricted Zone"
))

conn.commit()
conn.close()

print("Event added to database")
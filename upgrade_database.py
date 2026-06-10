import sqlite3

conn = sqlite3.connect("events.db")
cursor = conn.cursor()

try:
    cursor.execute("""
    ALTER TABLE events
    ADD COLUMN threat_level TEXT
    """)
    print("Threat level column added")

except Exception as e:
    print("Column may already exist:", e)

conn.commit()
conn.close()
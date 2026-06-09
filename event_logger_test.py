import csv
from datetime import datetime

with open("events.csv", "a", newline="") as file:
    writer = csv.writer(file)

    writer.writerow([
        datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        1,
        "Entered Restricted Zone"
    ])

print("Event logged successfully")
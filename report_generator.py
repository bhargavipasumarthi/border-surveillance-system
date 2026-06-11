from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

from reportlab.lib.styles import getSampleStyleSheet
import sqlite3

# Create PDF
pdf = SimpleDocTemplate(
    "Incident_Report.pdf"
)

styles = getSampleStyleSheet()

content = []

title = Paragraph(
    "Border Surveillance Incident Report",
    styles["Title"]
)

content.append(title)
content.append(Spacer(1, 20))

# Read database
conn = sqlite3.connect("events.db")

cursor = conn.cursor()

cursor.execute(
    """
    SELECT timestamp,
           object_id,
           event,
           threat_level
    FROM events
    ORDER BY id DESC
    """
)

rows = cursor.fetchall()

conn.close()
content.append(
    Paragraph(
        f"Total Events: {len(rows)}",
        styles["Heading2"]
    )
)

content.append(
    Spacer(1, 10)
)

# Add events
for row in rows:

    timestamp, object_id, event, threat = row

    text = (
        f"<b>Time:</b> {timestamp}<br/>"
        f"<b>Object ID:</b> {object_id}<br/>"
        f"<b>Event:</b> {event}<br/>"
        f"<b>Threat Level:</b> {threat}"
    )

    content.append(
        Paragraph(
            text,
            styles["BodyText"]
        )
    )

    content.append(
        Spacer(1, 12)
    )

pdf.build(content)

print("✅ Incident_Report.pdf generated")
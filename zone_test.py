from db_logger import log_event
import csv
from datetime import datetime
from ultralytics import YOLO
import supervision as sv
import cv2

# Load model
model = YOLO("yolov8n.pt")

# Tracker
tracker = sv.ByteTrack()

# Open video
cap = cv2.VideoCapture("test.mp4")

# Restricted zone coordinates
ZONE_X1 = 50
ZONE_Y1 = 50

ZONE_X2 = 1000
ZONE_Y2 = 700

alerted_ids = set()

while cap.isOpened():

    success, frame = cap.read()

    if not success:
        break

    result = model(frame)[0]

    detections = sv.Detections.from_ultralytics(result)

    detections = tracker.update_with_detections(
        detections
    )

    # Draw restricted zone
    cv2.rectangle(
        frame,
        (ZONE_X1, ZONE_Y1),
        (ZONE_X2, ZONE_Y2),
        (0, 0, 255),
        3
    )

    cv2.putText(
        frame,
        "RESTRICTED ZONE",
        (ZONE_X1, ZONE_Y1 - 10),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (0, 0, 255),
        2
    )

    for bbox, tracker_id, class_id in zip(
    detections.xyxy,
    detections.tracker_id,
    detections.class_id
):

        x1, y1, x2, y2 = map(int, bbox)
        object_name = model.names[int(class_id)]

        center_x = (x1 + x2) // 2
        center_y = (y1 + y2) // 2

        # Draw object
        cv2.rectangle(
            frame,
            (x1, y1),
            (x2, y2),
            (0, 255, 0),
            2
        )

        cv2.putText(
            frame,
            f"ID {tracker_id}",
            (x1, y1 - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (0, 255, 0),
            2
        )

        # Draw center point
        cv2.circle(
            frame,
            (center_x, center_y),
            5,
            (255, 0, 0),
            -1
        )

        # Check if inside zone
        inside_zone = (
            ZONE_X1 <= center_x <= ZONE_X2
            and
            ZONE_Y1 <= center_y <= ZONE_Y2
        )

    if inside_zone and tracker_id not in alerted_ids:

        alerted_ids.add(tracker_id)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

        filename = f"evidence/intrusion_ID{tracker_id}_{timestamp}.jpg"

        cv2.imwrite(filename, frame)

        print(f"📸 Screenshot saved: {filename}")

        print(
            f"🚨 ALERT: ID {tracker_id} entered restricted zone"
        )
        threat = get_threat_level(object_name)

        log_event(
            tracker_id,
            "Entered Restricted Zone",
            threat
)

        with open("events.csv", "a", newline="") as file:
            writer = csv.writer(file)

            writer.writerow([
                datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                tracker_id,
                "Entered Restricted Zone"
        ])

    cv2.imshow(
        "Restricted Zone Detection",
        frame
    )

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
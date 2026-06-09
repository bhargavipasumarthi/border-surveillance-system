from ultralytics import YOLO
import supervision as sv
import cv2

# Load YOLO model
model = YOLO("yolov8n.pt")

# Initialize ByteTrack
tracker = sv.ByteTrack()

# Open video
cap = cv2.VideoCapture("test.mp4")

while cap.isOpened():
    success, frame = cap.read()

    if not success:
        break

    # Run detection
    result = model(frame)[0]

    # Convert YOLO detections to Supervision format
    detections = sv.Detections.from_ultralytics(result)

    # Update tracker
    detections = tracker.update_with_detections(detections)

    # Draw boxes and IDs
    annotated_frame = frame.copy()

    for bbox, tracker_id in zip(
        detections.xyxy,
        detections.tracker_id
    ):
        x1, y1, x2, y2 = map(int, bbox)

        cv2.rectangle(
            annotated_frame,
            (x1, y1),
            (x2, y2),
            (0, 255, 0),
            2
        )

        cv2.putText(
            annotated_frame,
            f"ID {tracker_id}",
            (x1, y1 - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (0, 255, 0),
            2
        )

    cv2.imshow("Tracking", annotated_frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
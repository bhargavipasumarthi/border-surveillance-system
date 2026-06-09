from ultralytics import YOLO
import supervision as sv
import cv2

model = YOLO("yolov8n.pt")
tracker = sv.ByteTrack()

cap = cv2.VideoCapture("test.mp4")

BORDER_Y = 300

crossed_ids = set()

while cap.isOpened():
    success, frame = cap.read()

    if not success:
        break

    result = model(frame)[0]

    detections = sv.Detections.from_ultralytics(result)
    detections = tracker.update_with_detections(detections)

    cv2.line(
        frame,
        (0, BORDER_Y),
        (frame.shape[1], BORDER_Y),
        (0, 0, 255),
        3
    )

    for bbox, tracker_id in zip(
        detections.xyxy,
        detections.tracker_id
    ):
        x1, y1, x2, y2 = map(int, bbox)

        center_y = (y1 + y2) // 2

        print(
            f"ID {tracker_id} | Center Y = {center_y}"
        )

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

        if center_y > BORDER_Y and tracker_id not in crossed_ids:
            crossed_ids.add(tracker_id)

            print(
                f"ALERT: Object ID {tracker_id} crossed border"
            )

    cv2.imshow("Border Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
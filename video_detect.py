from ultralytics import YOLO
import cv2

print("Program started")

model = YOLO("yolov8n.pt")

video_path = "test.mp4"
print(f"Trying to open: {video_path}")

cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    print("ERROR: Could not open video")
    exit()

print("Video opened successfully")

while True:
    success, frame = cap.read()

    if not success:
        print("No more frames")
        break

    print("Processing frame")

    results = model(frame)

    annotated_frame = results[0].plot()

    cv2.imshow("Detection", annotated_frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()

print("Finished")
from ultralytics import YOLO


model = YOLO("yolov8n.pt")


results = model("https://ultralytics.com/images/bus.jpg")


results[0].show()


for box in results[0].boxes:
    class_id = int(box.cls[0])
    confidence = float(box.conf[0])

    print(
        f"Class: {model.names[class_id]}, "
        f"Confidence: {confidence:.2f}"
    )
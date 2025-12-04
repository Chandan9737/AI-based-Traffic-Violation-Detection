from ultralytics import YOLO
import cv2
import os

# Load YOLOv8 model (you will place yolov8n.pt or your custom model inside yolov8_model/)

model = YOLO("yolov8_model/yolov8n.pt")

# Violation target labels (modify based on dataset)

HELMET_LABELS = ["no_helmet", "without_helmet", "helmetless", "helmet"]  # Helmet class reference
BIKE_LABEL = "motorcycle"
TRIPLE_RIDING_LABEL = "triple_riding"
SIGNAL_LABEL = "signal"

def detect_violations(source, mode="image"):
os.makedirs("output", exist_ok=True)

```
if mode == "image":
    img = cv2.imread(source)
    results = model(img)
    annotated = results[0].plot()

    output_path = f"output/result.jpg"
    cv2.imwrite(output_path, annotated)
    print(f"[✔] Output saved as {output_path}")

    cv2.imshow("Result", annotated)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

elif mode == "video":
    cap = cv2.VideoCapture(source)
    fourcc = cv2.VideoWriter_fourcc(*"mp4v")
    out = cv2.VideoWriter("output/result_video.mp4", fourcc, 20.0,
                          (int(cap.get(3)), int(cap.get(4))))

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        results = model(frame)
        annotated = results[0].plot()
        out.write(annotated)

        cv2.imshow("Traffic Detection", annotated)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cap.release()
    out.release()
    cv2.destroyAllWindows()
    print("[✔] Video output saved to output
```

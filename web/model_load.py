from ultralytics import YOLO

model = YOLO("yolov8n")
model = YOLO("model/last.pt")
results = model.predict('./downimage/no_helmet.jpg', conf=0.05, iou=0.65, max_det=300, save=True)
for result in results:
    labels = result.boxes.cls
    scores = result.boxes.conf
    bboxes = result.boxes.xyxy
    print(labels)

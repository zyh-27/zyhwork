from ultralytics import YOLO

# 加载轻量化YOLOv8n模型
model = YOLO("yolov8n.yaml")

if __name__ == "__main__":
    # 开始训练
    results = model.train(
        data="src/dataset.yaml",
        epochs=50,
        imgsz=640,
        batch=8,
        device="cpu"
    )
    print("模型训练完成")

from ultralytics import YOLO
import os
import shutil

# 固定工作目录为项目根目录（本文件位于 src/ 下，上一级即为项目根）
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(BASE_DIR)

# 优先加载训练生成的自训权重 model/best.pt，不存在时回退官方预训练权重
best_pt = os.path.join(BASE_DIR, "model", "best.pt")
model = YOLO(best_pt if os.path.exists(best_pt) else "yolov8n.pt")

# 对原始图片做缺陷检测（固定输出到 runs/detect/predict，避免目录递增）
model.predict(
    os.path.join(BASE_DIR, "data", "test_imgs"),
    save=True,
    project=os.path.join(BASE_DIR, "runs", "detect"),
    name="predict",
    exist_ok=True,
)

# 把效果图复制到 result 文件夹
source = os.path.join(BASE_DIR, "runs", "detect", "predict")
target = os.path.join(BASE_DIR, "result")

os.makedirs(target, exist_ok=True)

if os.path.exists(source):
    copied = 0
    for f in os.listdir(source):
        if f.lower().endswith((".jpg", ".jpeg", ".png")):
            shutil.copy(os.path.join(source, f), os.path.join(target, f))
            copied += 1
    print(f"检测效果图已保存到 result 文件夹（共 {copied} 张）")
else:
    print("未找到检测输出目录")

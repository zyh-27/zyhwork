from ultralytics import YOLO
import os
import shutil

# 固定工作目录为项目根目录（本文件位于 src/ 下，上一级即为项目根）
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(BASE_DIR)

# 使用YOLOv8官方预训练权重做演示（不需要自己训练）
model = YOLO("yolov8n.pt")

# 对原始图片做检测
model.predict("data/test_imgs", save=True)
# 检测结果自动保存在 runs/detect/predict

# 把效果图复制到 result 文件夹
source = "runs/detect/predict"
target = "result"

os.makedirs(target, exist_ok=True)

if os.path.exists(source):
    for f in os.listdir(source):
        shutil.copy(os.path.join(source, f), os.path.join(target, f))
    print("检测效果图已保存到 result 文件夹")
else:
    print("未找到检测输出目录")

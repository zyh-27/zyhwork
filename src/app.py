from ultralytics import YOLO
import gradio as gr
import os

# 项目根目录（本文件位于 src/ 下），确保从任意位置运行都能找到权重
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
model = YOLO(os.path.join(BASE_DIR, "yolov8n.pt"))

def detect(img):
    res = model.predict(img, save=False)
    return res[0].plot()

demo = gr.Interface(
    fn=detect,
    inputs=gr.Image(type="numpy", label="上传PCB图片"),
    outputs=gr.Image(label="缺陷检测结果")
)

if __name__ == "__main__":
    demo.launch()

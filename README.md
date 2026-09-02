## 第三阶段：数据准备阶段
### 1.数据来源
项目使用公开开源数据集DeepPCB。
数据集链接：
github原版：https://github.com/tangsanli5201/DeepPCB
国内镜像：https://gitcode.com/gh_mirrors/de/DeepPCB
完整数据集本地保存，仓库`data/`目录存放测试样本、预处理输出文件以及数据集说明文档。

### 2.数据预处理工作
1.编写图像预处理脚本，功能包含：灰度转换、高斯滤波降噪、直方图均衡化、ROI感兴趣区域裁剪、图像尺寸归一化。
2.对原始PCB图像做数据增广：图像翻转、旋转、亮度扰动，扩充样本数量。
3.预处理完成后输出处理后的图片保存至`data/processed/`，同时生成样本索引文件，供算法模块调用。

### 3.AI提示词追溯
创建`prompt/`目录，每个开发阶段把和AI交互记录保存为json文件，上下文压缩前完成备份，随版本提交到git仓库。当前阶段文件：`prompt/stage3_data_prepare.json`

## 第四阶段：算法与模型训练推理阶段
### 1. 算法选型
采用YOLOv8n轻量化目标检测模型完成PCB缺陷检测。YOLOv8n参数量约3.2M，Anchor-Free解耦头设计，兼顾检测精度与CPU推理实时性，官方提供预训练权重，适合课程设计阶段快速验证完整检测流程。

### 2. 数据集格式转换与模型训练说明
- DeepPCB原始数据以txt格式保存缺陷标注（open/short/mousebite/spur/copper/pinhole六类，类别1-6），经`convert_to_yolo.py`转换为YOLO格式（类别0-5，归一化坐标），转换后数据组织为`data/yolo/images/{train,val}`与`data/yolo/labels/{train,val}`，共1000张训练、500张验证。
- 训练命令：`python src/train.py`（配置见`src/dataset.yaml`）
- 已在CPU环境完成10轮训练，验证集指标：mAP50=0.91、mAP50-95=0.661，六类缺陷识别率0.709~0.977，最优权重`model/best.pt`。

### 3. 推理演示
推理脚本`python src/detect.py`优先加载自训权重`model/best.pt`（不存在时回退官方预训练权重`yolov8n.pt`），对`data/test_imgs/`测试样本执行缺陷检测，检测效果图保存至`runs/detect/predict`并复制归档到`result/`目录，缺陷框标注类别与置信度（如`open 0.88`、`short 0.81`）。

### 4. AI提示词追溯
第四阶段AI交互记录归档文件：`prompt/stage4_pcb_chat.json`

## 第五阶段：Web可视化界面阶段
### 1. 技术选型
采用Gradio轻量级机器学习演示框架构建Web可视化界面，底层由FastAPI驱动，支持上传图片、实时推理、结果可视化，无需单独开发前后端，适合课程设计快速验证。

### 2. 界面功能
- 图片上传组件：`gr.Image(type="numpy")`，将上传图片解析为numpy数组供YOLO直接推理
- 缺陷检测：调用自训权重（`model/best.pt`，缺失时回退`yolov8n.pt`）实时推理，返回`res[0].plot()`带框标注结果图
- 结果展示：`gr.Image`组件渲染缺陷检测效果图，标注open/short/mousebite/spur/copper/pinhole六类缺陷及置信度

### 3. 运行方式
```bash
python src/app.py
```
浏览器打开 `http://127.0.0.1:7860`，上传PCB图片即可查看缺陷检测结果。

### 4. 验证结果
浏览器实测上传缺陷样本（`data/test_imgs/90100009.jpg`等），成功检测并标注open/short/copper/pinhole/spur等缺陷，Web界面截图归档：`result/web_demo_04.png`，自训权重检测效果图归档：`result/90100009.jpg`等

### 5. AI提示词追溯
第五阶段AI交互记录归档文件：`prompt/stage5_pcb_chat.json`

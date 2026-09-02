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

### 2. 模型训练说明
- DeepPCB原始数据以Matlab格式保存缺陷标注（open/short/mousebite/spur/copper/pinhole六类），需先转换为YOLO格式后执行训练：按`images/train`、`images/val`、`labels`目录组织数据，标签转为归一化txt文件。
- 训练命令：`python src/train.py`（配置见`src/dataset.yaml`）
- 受本机硬件（CPU）及数据集格式限制，完整50轮训练需在具备算力设备上执行，训练完成后生成的最优权重为`model/best.pt`。

### 3. 推理演示
演示阶段使用YOLOv8n官方预训练权重（`yolov8n.pt`）对`data/test_imgs/`测试样本执行缺陷检测，验证数据加载、模型推理、结果保存完整链路。运行命令：`python src/detect.py`，检测效果图自动保存至`runs/detect/predict`并复制归档到`result/`目录。

### 4. AI提示词追溯
第四阶段AI交互记录归档文件：`prompt/stage4_pcb_chat.json`

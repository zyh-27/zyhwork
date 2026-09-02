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
## 数据准备阶段说明
1. 原始测试样本目录：`data/test_imgs`，共3‑5张PCB缺陷图片
2. 图像预处理结果输出目录：`data/processed`
3. 本阶段完成操作：图像灰度化预处理
4. 后续模型训练使用公开数据集 DeepPCB

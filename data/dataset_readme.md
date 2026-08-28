# PCB电路板缺陷数据集说明
## 1.数据集来源
本项目采用开源DeepPCB数据集
github原版：https://github.com/tangsanli5201/DeepPCB
国内镜像(访问稳定)：https://gitcode.com/gh_mirrors/de/DeepPCB

## 2.数据集介绍
DeepPCB为工业PCB电路板缺陷公开数据集，包含1500组图像，包含6类PCB常见缺陷：
- open 开路
- short 短路
- mouse_bite 鼠咬
- spur 毛刺
- pin_hole 针孔
- spurious_copper 伪铜

数据集包含原始缺陷图、无缺陷模板图、标注文件，适配YOLO目标检测训练。

## 3.仓库存储说明
> 完整原始数据集文件体积较大，**完整训练集不上传GitHub仓库，本地留存使用**。
仓库内仅存放：
1. `test_imgs/`：少量PCB测试样本图片，用于系统演示测试
2. `processed/`：经过预处理后的图像与文件索引，由预处理脚本生成

## 4.数据划分
- train：训练集
- val：验证集
- test：测试集

## 5.数据集协议
开源学术数据集，可用于课程设计、学术研究。

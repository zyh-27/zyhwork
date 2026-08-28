# preprocess.py PCB图像预处理脚本
import cv2
import os

def preprocess_pcb(img_path,save_path):
    img=cv2.imread(img_path)
    #灰度化
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    #高斯滤波降噪
    blur=cv2.GaussianBlur(gray,(3,3),0)
    #直方图均衡化增强
    equ=cv2.equalizeHist(blur)
    #统一尺寸
    resized=cv2.resize(equ,(640,640))
    cv2.imwrite(save_path,resized)

if __name__=="__main__":
    test_img_dir="./data/test_imgs"
    out_dir="./data/processed"
    os.makedirs(out_dir,exist_ok=True)
    for name in os.listdir(test_img_dir):
        if name.endswith((".jpg",".png")):
            preprocess_pcb(os.path.join(test_img_dir,name),os.path.join(out_dir,name))

import os
import cv2

# ----------------------路径配置（自动获取py文件所在目录，不受终端位置影响）----------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# 测试图片文件夹，放在代码同目录下 data/test_imgs
test_img_dir = os.path.join(BASE_DIR, "data", "test_imgs")
# 预处理输出保存目录
output_dir = os.path.join(BASE_DIR, "data", "processed")

# 文件夹不存在就自动创建，不会报路径错误
os.makedirs(test_img_dir, exist_ok=True)
os.makedirs(output_dir, exist_ok=True)

# ----------------------打印调试信息，方便排查问题----------------------
print(f"【脚本所在目录】{BASE_DIR}")
print(f"【待读取图片目录】{test_img_dir}")

# 获取文件夹全部文件，兼容jpg png jpeg
all_files = os.listdir(test_img_dir)
print(f"【文件夹全部文件列表】{all_files}")

img_name_list = [f for f in all_files if f.lower().endswith((".jpg", ".png", ".jpeg"))]
print(f"【筛选出来的图片文件】{img_name_list}")

if len(img_name_list) == 0:
    print("⚠️警告：没有找到图片！请把PCB图片放到 data/test_imgs 文件夹里面！")
else:
    print(f"✅一共找到 {len(img_name_list)} 张图片，开始预处理")
    # 图像预处理循环
    for img_name in img_name_list:
        img_path = os.path.join(test_img_dir, img_name)
        img = cv2.imread(img_path)

        if img is None:
            print(f"❌读取失败：{img_name}")
            continue

        # ----------------PCB预处理操作，你可以按需修改----------------
        # 1.缩放统一尺寸
        img_resize = cv2.resize(img, (640, 640))
        # 2.灰度化
        img_gray = cv2.cvtColor(img_resize, cv2.COLOR_BGR2GRAY)
        # 3.高斯模糊降噪
        img_blur = cv2.GaussianBlur(img_gray, (3, 3), 0)

        # 保存处理完成图片
        save_path = os.path.join(output_dir, img_name)
        cv2.imwrite(save_path, img_blur)
        print(f"✅处理完成保存：{img_name}")
print("\n🎉全部执行结束")

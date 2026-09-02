# -*- coding: utf-8 -*-
"""
DeepPCB 数据集转 YOLO 格式脚本
- 读取 DeepPCB 的 trainval.txt / test.txt 文件列表
- 将 x1 y1 x2 y2 类别(1-6) 标注转换为 YOLO 归一化 txt 标签（类别 0-5）
- 输出到 data/yolo/ 目录：images/{train,val}、labels/{train,val}
"""
import os
import shutil

BASE = r"C:\Users\29270\Desktop\DeepPCB-master\PCBData"
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data", "yolo")
IMG_W = IMG_H = 640  # DeepPCB 图片尺寸


def convert(split_file, split_name):
    img_dir = os.path.join(OUT, "images", split_name)
    lbl_dir = os.path.join(OUT, "labels", split_name)
    os.makedirs(img_dir, exist_ok=True)
    os.makedirs(lbl_dir, exist_ok=True)

    count = 0
    with open(os.path.join(BASE, split_file), encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            img_rel, lbl_rel = line.split()
            # img_rel 形如 group20085/20085/20085291.jpg
            parts = img_rel.split("/")
            img_id = os.path.splitext(parts[2])[0]  # 20085291
            # 实际缺陷测试图为 {id}_test.jpg
            img_src = os.path.join(BASE, parts[0], parts[1], img_id + "_test.jpg")
            lbl_src = os.path.join(BASE, lbl_rel)

            if not os.path.exists(img_src):
                print("[SKIP] 缺图片:", img_src)
                continue
            if not os.path.exists(lbl_src):
                print("[SKIP] 缺标注:", lbl_src)
                continue

            shutil.copy(img_src, os.path.join(img_dir, img_id + ".jpg"))

            out_lines = []
            with open(lbl_src, encoding="utf-8") as lf:
                for l in lf:
                    l = l.strip()
                    if not l:
                        continue
                    fields = l.split()
                    if len(fields) < 5:
                        continue
                    x1, y1, x2, y2, cls = float(fields[0]), float(fields[1]), float(fields[2]), float(fields[3]), int(fields[4])
                    cx = ((x1 + x2) / 2.0) / IMG_W
                    cy = ((y1 + y2) / 2.0) / IMG_H
                    w = (x2 - x1) / IMG_W
                    h = (y2 - y1) / IMG_H
                    cls_yolo = cls - 1  # DeepPCB 类别 1-6 -> YOLO 0-5
                    out_lines.append(f"{cls_yolo} {cx:.6f} {cy:.6f} {w:.6f} {h:.6f}")

            with open(os.path.join(lbl_dir, img_id + ".txt"), "w", encoding="utf-8") as wf:
                wf.write("\n".join(out_lines))
            count += 1

    print(f"[完成] {split_name}: {count} 张图片已转换")


if __name__ == "__main__":
    convert("trainval.txt", "train")
    convert("test.txt", "val")
    print("全部转换完成，输出目录:", OUT)

# pip install onnxruntime==1.4.0

import onnxruntime as rt

MODEL_PATH=""
sess = rt.InferenceSession(MODEL_PATH)



mean = (0.485, 0.456, 0.406)
std = (0.229, 0.224, 0.225)

import cv2
import numpy as np
# 用于将图像输入模型进行推理，并对输出结果进行后处理，得到最终的边界框和相应的置信度分数
def process(self, img, short_size):
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    h, w = img.shape[:2]
    if h < w:
        scale_h = short_size / h
        tar_w = w * scale_h
        tar_w = tar_w - tar_w % 32
        tar_w = max(32, tar_w)
        scale_w = tar_w / w
    else:
        scale_w = short_size / w
        tar_h = h * scale_w
        tar_h = tar_h - tar_h % 32
        tar_h = max(32, tar_h)
        scale_h = tar_h / h

        img = cv2.resize(img, None, fx=scale_w, fy=scale_h)

        img = img.astype(np.float32)

        img /= 255.0
        img -= mean
        img /= std
        img = img.transpose(2, 0, 1)
        transformed_image = np.expand_dims(img, axis=0)
        out = sess.run(["out1"], {"input0": transformed_image.astype(np.float32)})
        box_list, score_list = decode_handel(out[0][0], h, w)
        if len(box_list) > 0:
            idx = box_list.reshape(box_list.shape[0], -1).sum(axis=1) > 0  # 去掉全为0的框
            box_list, score_list = box_list[idx], score_list[idx]
        else:
            box_list, score_list = [], []
        return box_list, score_list






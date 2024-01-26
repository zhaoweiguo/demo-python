from PIL import Image, ImageDraw,ImageFont

import os
import logging

# 获取当前文件所在的目录
current_directory = os.path.dirname(os.path.abspath(__file__))

# 设置工作目录
os.chdir(current_directory)


LOGGER_ROOT_NAME = 'TTTTTest'
logger = logging.getLogger(LOGGER_ROOT_NAME)
logger.setLevel(logging.INFO)



img = Image.open("../data/a.png")
# print(img)

# 确保 img 对象有 EXIF（Exchangeable image file format）数据。
# EXIF 数据通常包含有关图像的信息，例如拍摄时间、相机型号、光圈、快门速度等
# print(hasattr(img, '_getexif'))
# print(img._getexif())

# 确保在显示图像时它们被正确地旋转
try:
    if hasattr(img, '_getexif') and img._getexif() is not None:
        orientation = 274
        exif = dict(img._getexif().items())
        if orientation not in exif:
            exif[orientation] = 0
        if exif[orientation] == 3:
            img = img.rotate(180, expand=True)
        elif exif[orientation] == 6:
            img = img.rotate(270, expand=True)
        elif exif[orientation] == 8:
            img = img.rotate(90, expand=True)
except Exception as ex:
    logger.error(ex.__str__, exc_info=True)



img = img.convert("RGB")
print(img.size)

short_size = 960


from model import  OcrHandle
ocrhandle = OcrHandle()
res = ocrhandle.text_predict(img, short_size)

img_detected = img.copy()
img_draw = ImageDraw.Draw(img_detected)
colors = ['red', 'green', 'blue', "purple"]


# 在图像上绘制检测到的文本区域的边框和序号
for i, r in enumerate(res):
    rect, txt, confidence = r

    x1,y1,x2,y2,x3,y3,x4,y4 = rect.reshape(-1)

    size = max(min(x2-x1,y3-y2) // 2 , 20 )   # 计算文本绘制时所需的字体大小
    myfont = ImageFont.truetype(os.path.join(os.getcwd(), "仿宋_GB2312.ttf"), size=size)
    fillcolor = colors[i % len(colors)]

    img_draw.text((x1, y1 - size ), str(i+1), font=myfont, fill=fillcolor)
    for xy in [(x1, y1, x2, y2), (x2, y2, x3, y3 ), (x3 , y3 , x4, y4), (x4, y4, x1, y1)]:
        img_draw.line(xy=xy, fill=colors[i % len(colors)], width=2)


img_detected.save("../output/a.png", format='JPEG')









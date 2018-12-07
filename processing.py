import cv2
import numpy as np
from PIL import Image
from matplotlib import pyplot as plt



def PIL_img2CV_img(PILimg):
    CVimg = cv2.cvtColor(np.asarray(PILimg), cv2.COLOR_RGB2BGR)
    return CVimg


def CV_img2PIL_img(CVimg):
    PILimg = Image.fromarray(cv2.cvtColor(CVimg, cv2.COLOR_BGR2RGB))
    return PILimg


def hist_eql(pil_img):
    cv_img = PIL_img2CV_img(pil_img)
    gray = cv2.cvtColor(cv_img, cv2.COLOR_BGR2GRAY)
    save_hist(gray, 'left')
    # equalize Hist方法 直方图均衡化
    CV_img_eq = cv2.equalizeHist(gray)
    save_hist(CV_img_eq, 'right')

    # 将灰色通道图和均衡化结果 转回BGR通道
    CV_img_eq = cv2.cvtColor(CV_img_eq, cv2.COLOR_GRAY2BGR)
    CV_img_gray = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)

    # 变换为BIL图返回
    PIL_img_gray = CV_img2PIL_img(CV_img_gray)
    PIL_img_eq = CV_img2PIL_img(CV_img_eq)
    return PIL_img_eq, PIL_img_gray


def save_hist(cv_img, side):
    hist = cv2.calcHist([cv_img], [0], None, [256], [0, 256])
    f = plt.figure()  # 新建一个图像
    plt.title("Grayscale Histogram")  # 图像的标题
    plt.xlabel("Bins")  # X轴标签
    plt.ylabel("# of Pixels")  # Y轴标签
    plt.plot(hist)  # 画图
    plt.xlim([0, 256])  # 设置x坐标轴范围
    # plt.show()  # 显示图像
    plt.savefig('images/temp'+side)

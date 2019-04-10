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


def edge_detect(PIL_img):
    CV_img = PIL_img2CV_img(PIL_img)
    CV_gray = cv2.cvtColor(CV_img, cv2.COLOR_BGR2GRAY)
    # Canny函数，三个参数：源图像，低阈值，高阈值
    CV_detected = cv2.Canny(CV_img, 100, 300)
    return CV_img2PIL_img(cv2.cvtColor(CV_detected, cv2.COLOR_GRAY2BGR))


def Otus_hold(PIL_img):
    im = PIL_img.convert('L')
    mt = np.asarray(im)

    w,h = mt.shape
    grayScale = 256 # 灰度级256级
    pixCount = np.zeros(grayScale)   # 每个灰度值像素统计
    pixSum = w*h
    pixPro = np.zeros(256)     # 每个灰度值所占像素比例
    th = -1
    deltaMax = 0
    w0 = w1 = u0tmp = u1tmp = u0 = u1 =deltaTmp = 0
    for i in range(w):
        for j in range(h):
            pixCount[mt[i][j]] += 1

    for i in range(grayScale):
        pixPro[i] = pixCount[i] * 1.0/ pixSum
    
    
    for i in range(grayScale-1):  # 0~255灰度测试是哪一个
        w0 = w1 = u0tmp = u1tmp = u0 = u1 =deltaTmp = 0.0
        for j in range(grayScale-1):
            if j<=i:        # 背景
                w0 += float(pixPro[j])
                u0tmp += j * float(pixPro[j])
            else:           # 前景
                w1 += float(pixPro[j])
                u1tmp += j *float(pixPro[j])

        if float(w1)!=0.0 and float(w0) !=0.0:
            u0 = u0tmp /w0
            u1 = u1tmp /w1        
            deltaTmp = w0*w1*(u0-u1)**2
            if deltaTmp > deltaMax: 
                deltaMax = deltaTmp
                th = i
    mt_c = mt.copy()

    for i in range(w):
        for j in range(h):
            if mt_c[i][j] >= th:
                mt_c[i][j] = 255
            else:
                mt_c[i][j] = 0
    
    im2 = Image.fromarray(mt_c)
    return im, im2
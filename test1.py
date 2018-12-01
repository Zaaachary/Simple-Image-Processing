import cv2
def detect(filename):
    # face_cascade 为CascadeClassifier对象
    face_cascade = cv2.CascadeClassifier('haarcascades/haarcascade_frontalface_default.xml')
    img = cv2.imread(filename)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # 转化为灰度图

    # # 参数：
    # # 待检测的灰度图
    # # 每次搜索图像时，搜索窗口的压缩率。1.3表示搜索窗口扩大30%
    # # 每个人脸矩形保留近邻数目的最小值
    faces = face_cascade.detectMultiScale(gray, 1.3, 5) # 返回人脸矩形数组

    # for (x, y, w, h) in faces:
    #     img = cv2.rectangle(img, (x,y), (x+w, y+h), (0, 255, 0), 2) #绘制矩形
    # cv2.imshow("face detect", img)
    # cv2.waitKey(0)

if __name__ == "__main__":
    detect('img/2.jpg')
import cv2
import tkinter as tk
 
img = None
def main(pic = '1.jpg'):
    global img
    
    img = cv2.imread(pic,0)
    cv2.imshow('image',img)
    #gui功能
    app = tk.Tk()
    app.title('功能')
    button = tk.Button(app,text='放大',fg='blue',command = button_fun)
    button.pack()
    app.mainloop()
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()
 
def button_fun():
    global img
    
    size = img.shape#获取图片大小（长，宽，通道数）
    tempimg = cv2.resize(img,(size[1]*2,size[0]*2),cv2.INTER_LINEAR)
    cv2.imshow('imag2',tempimg)
 
 
if __name__ == '__main__':
    main()

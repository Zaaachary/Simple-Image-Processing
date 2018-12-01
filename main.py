import tkinter as tk
from tkinter.filedialog import askopenfilename
import processing as pc
from PIL import Image, ImageTk

import matplotlib
from matplotlib.pylab import mpl
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg,NavigationToolbar2Tk #NavigationToolbar2TkAgg


image_file = None
originimage = None
proceimage = None


def resize(w, h, w_box, h_box, pil_image):
    '''
    resize a pil_image object so it will fit into
    a box of size w_box times h_box, but retain aspect ratio
    对一个pil_image对象进行缩放，让它在一个矩形框内，还能保持比例
    '''
    f1 = 1.0*w_box/w # 1.0 forces float division in Python2
    f2 = 1.0*h_box/h
    factor = min([f1, f2])
    #print(f1, f2, factor) # test
    # use best down-sizing filter
    width = int(w*factor)
    height = int(h*factor)
    # 使用resize进行缩放
    return pil_image.resize((width, height), Image.ANTIALIAS)


def open_image():
    global image_file
    # 用对话框询问文件路径
    filepath = askopenfilename()
    # 用Image打开图片
    image_file = Image.open(filepath)
    # 期望图像显示的大小
    w_box = 500
    h_box = 700
    # 缩放图像让它保持比例，同时限制在一个矩形框范围内
    w, h = image_file.size
    img_resize = resize(w, h, w_box, h_box, image_file)
    # 将image转换成ImageTk
    originimage = ImageTk.PhotoImage(image=img_resize)
    # imgleft更新图片
    imgleft.config(image=originimage)
    imgleft.image = originimage
    imgright.config(image=originimage)
    imgleft.image = originimage


def save_image():
    pass


def hst_eql():
    PILimg, PIL_gary = pc.hist_eql(image_file)
    # 期望图像显示的大小
    w_box = 500
    h_box = 700

    # 缩放图像让它保持比例，同时限制在一个矩形框范围内
    w, h = PIL_gary.size
    img_resize = resize(w, h, w_box, h_box, PIL_gary)
    # 将image转换成ImageTk
    originimage = ImageTk.PhotoImage(image=img_resize)
    # imgleft更新图片
    imgleft.config(image=originimage)
    imgleft.image = originimage
    draw_hist(PIL_gary,'left')

    # 缩放图像让它保持比例，同时限制在一个矩形框范围内
    w, h = PILimg.size
    img_resize = resize(w, h, w_box, h_box, PILimg)
    # 将image转换成ImageTk
    proceimage = ImageTk.PhotoImage(image=img_resize)
    # imgright更新图片
    imgright.config(image=proceimage)
    imgright.image = proceimage
    draw_hist(PILimg,'right')



def draw_hist(PIL_gary,side):
    if side =='left':
        figure = pc.drawHist(PIL_gary)
        canvasl = FigureCanvasTkAgg(figure, frm_left)
        canvasl.draw()
        canvasl.get_tk_widget().pack(side=tk.TOP,fill=tk.BOTH,expand=1)
    else:
        figure = pc.drawHist(PIL_gary)
        canvasr = FigureCanvasTkAgg(figure, frm_right)
        canvasr.draw()
        canvasr.get_tk_widget().pack(side=tk.TOP,fill=tk.BOTH,expand=1)


def edge():
    pass




root = tk.Tk()
root.title('简单的图像处理')
root.geometry('1152x768')

# 菜单栏
menubar = tk.Menu(root)
filemenu = tk.Menu(menubar, tearoff=0)
filemenu.add_command(label='打开', command=open_image)
filemenu.add_command(label='保存', command=save_image)
operate = tk.Menu(menubar, tearoff=0)
operate.add_command(label='直方图均衡化', command=hst_eql)
operate.add_command(label='边缘检测', command=edge)
menubar.add_cascade(label='文件', menu=filemenu)
menubar.add_cascade(label='操作', menu=operate)

# 在window上创建一个frame
frm = tk.Frame(root)
frm.pack()
# 在创建好的frame上创建两个frame 即frm下有两个frame
frm_left = tk.Frame(frm)
frm_right = tk.Frame(frm)
# 控制两个小的frm在大的相对位置
frm_left.pack(side='left')
frm_right.pack(side='right')

imgleft = tk.Label(frm_left,bg='blue')
imgright = tk.Label(frm_right,bg='yellow')
imgleft.pack()
imgright.pack()

canvasl = tk.Canvas()
canvasr = tk.Canvas()


root.config(menu=menubar)
root.mainloop()

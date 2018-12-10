import tkinter as tk
from tkinter.filedialog import askopenfilename
import processing as pc
from PIL import Image, ImageTk

image_file = None
originimage = None
proceimage = None


def resize(w, h, w_box, h_box, pil_image):
    '''
    resize a pil_image object so it will fit into
    a box of size w_box times h_box, but retain aspect ratio
    对一个pil_image对象进行缩放，让它在一个矩形框内，还能保持比例
    '''
    f1 = 1.0 * w_box / w  # 1.0 forces float division in Python2
    f2 = 1.0 * h_box / h
    factor = min([f1, f2])
    # print(f1, f2, factor) # test
    # use best down-sizing filter
    width = int(w * factor)
    height = int(h * factor)
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
    h_box = 350
    showimg(image_file, imgleft, w_box, h_box)
    showimg(image_file, imgright, w_box, h_box)


def save_image():
    global proceimage
    proceimage.save('images/processed.jpg')


def hst_eql():
    global proceimage
    PIL_eq, PIL_gary = pc.hist_eql(image_file)
    proceimage = PIL_eq
    # 期望图像显示的大小
    w_box = 500
    h_box = 350
    showimg(PIL_gary, imgleft, w_box, h_box)
    histO = Image.open('images/templeft.png')
    showimg(histO, histleft, w_box, h_box)

    showimg(PIL_eq, imgright, w_box, h_box)
    histE = Image.open('images/tempright.png')
    showimg(histE, histright, w_box, h_box)
    # pc.drawHist(PIL_img,'right')
    # draw_hist(PILimg, 'right')


def showimg(PIL_img, master, width, height):
    """
    :param PIL_img:要显示的图片
    :param master: 需要在这个元素中显示
    :param width: 期望的最大宽度
    :param height: 期望的最大高度
    :return: nothing
    """
    # 获取图像参数
    w, h = PIL_img.size
    # 缩放图像
    img_resize = resize(w, h, width, height, PIL_img)
    # Image 2 ImageTk
    Tk_img = ImageTk.PhotoImage(image=img_resize)
    # master显示图片
    master.config(image=Tk_img)
    master.image = Tk_img


def edge():
    PIL_detect = pc.edge_detect(image_file)
    global proceimage 
    proceimage = PIL_detect
    # 期望图像显示的大小
    w_box = 500
    h_box = 350
    showimg(image_file, imgleft, w_box, h_box)
    showimg(PIL_detect, imgright, w_box, h_box)
    histleft.config(image=None)
    histleft.image = None
    histright.config(image=None)
    histright.image = None


root = tk.Tk()
root.title('简单的图像处理')
root.geometry('1100x700')
root.config(bg='white')

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
frm = tk.Frame(root, bg='white')
frm.pack()
# 在创建好的frame上创建两个frame 即frm下有两个frame
frm_left = tk.Frame(frm, bg='white')
frm_right = tk.Frame(frm, bg='white')
# 控制两个小的frm在大的相对位置
frm_left.pack(side='left')
frm_right.pack(side='right')

imgleft = tk.Label(frm_left, bg='white')
histleft = tk.Label(frm_left, bg='white')

imgright = tk.Label(frm_right, bg='white')
histright = tk.Label(frm_right, bg='white')
imgleft.pack()
histleft.pack()
imgright.pack()
histright.pack()
# canvasl = tk.Canvas(frm_left, bg='white').pack()
# canvasr = tk.Canvas(frm_right, bg='white').pack()


root.config(menu=menubar)
root.mainloop()

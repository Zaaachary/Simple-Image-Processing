import tkinter as tk
from tkinter.filedialog import askopenfilename

class Application:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title('简单的图像处理')
        self.root.geometry('1300x800')

        self.menubar = tk.Menu(self.root)
        self.filemenu = tk.Menu(self.menubar, tearoff=0)
        self.filemenu.add_command(label='打开', command=self.open_image)
        self.filemenu.add_command(label='保存', command=self.save_image)
        self.operate = tk.Menu(self.menubar, tearoff=0)
        self.operate.add_command(label='直方图均衡化', command=self.hst_eql)
        self.operate.add_command(label='边缘检测', command=self.edge)
        self.menubar.add_cascade(label='文件', menu=self.filemenu)
        self.menubar.add_cascade(label='操作', menu=self.operate)
        self.frm = tk.Frame(self.root)
        self.frm.pack()
        self.frm_left = tk.Frame(self.frm).pack(side='left')
        self.frm_right = tk.Frame(self.frm).pack(side='right')
        self.root.mainloop()

    def open_image(self):
        pass

    def save_image(self):
        pass

    def hst_eql(self):
        pass

    def edge(self):
        pass



if __name__ == '__main__':
    app = Application()
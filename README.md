# Simple-Image-Processing
An GUI image processing program written in python. The program based on opencv, tkinter and matplotlib,and it can achieve Grayscale Histogram Equalization, Threshold-based edge detection function.

This is my homework of the image processing course. My student ID is 2016217812.
## Uages Guide
### Execute
Execute `main.py` by using  `python main.py`. 
Click on "打开" and chose the picture you want to process, then you can chose 'Histogram equalization' or 'Edge recognition by Canny'. After the operation, you can save the image processed.
### Attention
**Before Executing the program**, you have to make sure that you have installed all the package related. This code is written by Python 3.6.6, and the related packages have been written in `packages-required.txt`, use command `pip install -r packages-required.txt` to install all these packages.
### Code
- main.py: GUI and program entry.
- processing.py: Image process function which will be used by main.py.

## Core Packages
- OpenCV
- Matplotlib
- Tkinter
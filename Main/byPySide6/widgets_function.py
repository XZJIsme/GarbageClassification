import sys
import os
import platform

from PySide6 import QtGui
from PyQt5 import  QtWidgets
import AI_stuff
from modules import *  # Ui_MainWindow() imported
from widgets import *
from croppicture import crop

import _thread


def choose_picture(self_, widgets=None):
    imgName, imgType = QFileDialog.getOpenFileName(None, "打开图片", "", "*.jpg;;*.png;;All Files(*)")
    widgets.lineEdit_basic_pic_addr.setText(imgName)
    try:
        from PIL import Image
        img = Image.open(imgName)
        w = img.width  # 图片的宽
        h = img.height  # 图片的高
        if (w / h) > (widgets.basicpicturelabel.width() / widgets.basicpicturelabel.height()):
            width = widgets.basicpicturelabel.width()
            height = int(h * (width / w))
        else:
            height = widgets.basicpicturelabel.height()
            width = int(w * (height / h))
        jpg = QtGui.QPixmap(imgName).scaled(width, height)
        widgets.basicpicturelabel.setAlignment(Qt.AlignCenter)
        widgets.basicpicturelabel.setPixmap(jpg)
        widgets.basicpicturelabel.setStyleSheet('font-size: 11px; color: #f8f8f2; padding-left: 10px; padding-right: 10px; padding-bottom: 2px;')
        # 删去 Label 的背景图
    except:
        widgets.lineEdit_basic_pic_addr.setText('请选择图片')

def msg(self_,widgets=None):
     m = QFileDialog.getExistingDirectory(None,"选取文件夹","C:/") # 起始路径
     widgets.lineEdit_basic_dir_addr.setText(m)

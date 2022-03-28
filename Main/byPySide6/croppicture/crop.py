from email.headerregistry import Address
from PyQt5.QtCore import QSize, Qt, QRect
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QApplication, QDialog, QGridLayout, QPushButton, QSpacerItem, QSizePolicy
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QGraphicsScene
import os.path

try:
    from .graphics import GraphicsView, GraphicsPixmapItem
except:
    from graphics import GraphicsView, GraphicsPixmapItem
 
 
class Form(QDialog):
    def __init__(self,widgets):
        super(Form, self).__init__()
        self.resize(1024, 768)
        address=widgets.lineEdit_basic_pic_addr.text()
        self.picture = address
        self.init_ui()
        # 视图背景颜色
        self.graphicsView.setBackgroundBrush(QColor(28, 31, 34))
        self.graphicsView.save_signal.connect(self.pushButton_save.setEnabled)
        self.pushButton_cut.clicked.connect(self.pushButton_cut_clicked)
        self.pushButton_save.clicked.connect(self.pushButton_save_clicked)
        self.pushButton_save.clicked.connect(self.close)
        # image_item = GraphicsPolygonItem()
        # image_item.setFlag(QGraphicsItem.ItemIsMovable)
        # self.scene.addItem(image_item)
 
    def init_ui(self):
        self.gridLayout = QGridLayout(self)
        self.pushButton_cut = QPushButton('裁剪', self)
        self.pushButton_cut.setCheckable(True)
        self.pushButton_cut.setMaximumSize(QSize(100, 16777215))
        self.gridLayout.addWidget(self.pushButton_cut, 0, 0, 1, 1)
        self.pushButton_save = QPushButton('确定', self)
        self.pushButton_save.setEnabled(False)
        self.gridLayout.addWidget(self.pushButton_save, 1, 0, 1, 1)
        spacerItem = QSpacerItem(20, 549, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 2, 0, 1, 1)
        self.graphicsView = GraphicsView(self.picture, self)
        self.graphicsView.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.graphicsView.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.gridLayout.addWidget(self.graphicsView, 0, 1, 3, 1)
 
    def pushButton_cut_clicked(self):
        if self.graphicsView.image_item.is_start_cut:
            self.graphicsView.image_item.is_start_cut = False
            self.graphicsView.image_item.setCursor(Qt.ArrowCursor)  # 箭头光标
        else:
            self.graphicsView.image_item.is_start_cut = True
            self.graphicsView.image_item.setCursor(Qt.CrossCursor)  # 十字光标
 
    def pushButton_save_clicked(self):
        rect = QRect(self.graphicsView.image_item.start_point.toPoint(),
                     self.graphicsView.image_item.end_point.toPoint())
        new_pixmap = self.graphicsView.image_item.pixmap().copy(rect)
        new_pixmap.save(r'crop.png')
 
def cropui(self,widgets=None):
    import sys
    app = QApplication(sys.argv)
    form = Form(widgets)
    form.show()
    app.exec_()
    from PIL import Image
    from PySide6 import QtGui
    img = Image.open(r'crop.png')
    w = img.width  # 图片的宽
    h = img.height  # 图片的高
    if (w / h) > (widgets.basicpicturelabel.width() / widgets.basicpicturelabel.height()):
                width = widgets.basicpicturelabel.width()
                height = int(h * (width / w))
    else:
                height = widgets.basicpicturelabel.height()
                width = int(w * (height / h))
    jpg = QtGui.QPixmap(r'crop.png').scaled(width, height)
    widgets.basicpicturelabel.setPixmap(jpg)

if __name__ == '__main__':
    adress='E:/项目实训/[PKY[06N]GN4SKX5{]30I4A.jpg'
    cropui(adress)
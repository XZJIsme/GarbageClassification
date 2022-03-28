import json
import sys
import os
import platform

import numpy as np
from PySide6 import QtGui

# import AI_stuff
import AI_stuff
from modules import *  # Ui_MainWindow() imported
from widgets import *
from croppicture import crop

os.environ["QT_FONT_DPI"] = "96"  # FIX Problem for High DPI and Scale above 100%

import _thread
import widgets_function


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.widgets = self.ui

        Settings.ENABLE_CUSTOM_TITLE_BAR = True  # 使用自定义标题栏

        # APP NAME
        self.setWindowTitle("Garbage Classification")

        # TOGGLE MENU; SET UI DEFINITIONS; QTableWidget PARAMETERS
        self.widgets.toggleButton.clicked.connect(
            lambda: UIFunctions.toggleMenu(self, True))  # ToDo: 检查 app_settings.py 里设置的颜色
        UIFunctions.uiDefinitions(self)
        # self.widgets.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        # 按钮
        self.widgets.btn_home.clicked.connect(self.buttonClick)  # 切换为基础模式界面
        self.widgets.btn_pro_switch.clicked.connect(self.buttonClick)  # 切换为 Pro 模式界面
        self.widgets.btn_settings.clicked.connect(self.buttonClick)  # 切换为设置界面
        self.widgets.btn_basic_garbage_classification.clicked.connect(self.buttonClick)  # 垃圾识别
        self.widgets.btn_basic_feedback.clicked.connect(self.buttonClick)
        self.widgets.btn_basic_choose_pic.clicked.connect(self.buttonClick)
        self.widgets.btn_basic_crop.clicked.connect(self.buttonClick)
        self.widgets.btn_basic_choose_dir.clicked.connect(self.buttonClick)
        self.widgets.btn_page_feedback_submit.clicked.connect(self.buttonClick)
        self.widgets.btn_pro_start_training.clicked.connect(self.buttonClick)
        self.widgets.btn_basic_batch_classification.clicked.connect(self.buttonClick)
        # self.widgets.btn_pro_choose_premodel.clicked.connect(self.buttonClick)
        # self.widgets.btn_basic_choose_model.clicked.connect(self.buttonClick)
        self.widgets.comboBox_setting_default_net_choooser.currentTextChanged.connect(self.comboChanged)
        self.widgets.btn_basic_feedback.setEnabled(False)

        # checkbox
        # self.widgets.checkBox_pro_pretrain.stateChanged.connect(self.checkboxClick)
        self.widgets.checkBox_basic_default_model.stateChanged.connect(self.checkboxClick)

        # EXTRA LEFT BOX
        def openCloseLeftBox():
            UIFunctions.toggleLeftBox(self, True)

        # 检查训练参数
        self.widgets.label.setText('')
        self.widgets.lineEdit_pro_lr.textChanged.connect(self.checkTrainingArguments)
        self.widgets.lineEdit_pro_batch.textChanged.connect(self.checkTrainingArguments)
        self.widgets.lineEdit_pro_epoch.textChanged.connect(self.checkTrainingArguments)
        self.widgets.lineEdit_pro_saveevery_epoch.textChanged.connect(self.checkTrainingArguments)

        self.widgets.extraCloseColumnBtn.clicked.connect(openCloseLeftBox)

        # SHOW APP
        self.show()
        self.widgets.stackedWidget.setCurrentWidget(self.widgets.page_welcome)

        # 加载 qss 样式
        useCustomTheme = False
        themeFile = "themes\py_dracula_dark.qss"
        if useCustomTheme:
            # LOAD AND APPLY STYLE
            UIFunctions.theme(self, themeFile, True)
            # SET HACKS
            AppFunctions.setThemeHack(self)

        comboBoxList = []
        for i in range(0, 40):
            dic = open('垃圾数据字典.json', mode='r', encoding='utf-8').read()
            dic = json.loads(dic)
            n = dic['garbage'][str(i)]['name']
            c = dic['garbage'][str(i)]['classification']
            c = dic['classification'][str(c)]
            comboBoxList.append(str(i) + ' ' + n + ' ' + c)
        self.widgets.comboBox_feedback.insertItems(0, comboBoxList)

        # 接收后端消息
        import client_listener
        _thread.start_new_thread(client_listener.client_listener, (self.widgets, '', 11000))

        # 初始化连接
        try:
            _thread.start_new_thread(AI_stuff.connectServer, (self.widgets, AI_stuff.readLocalIP(), 23333))
        except:
            self.widgets.textBrowser_basic_log.insertHtml(
                '''<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#3a534c;">''' + '''<br>无法连接服务器，请尝试重新重启软件''' + '''</span></p>''')
        # self.widgets.comboBox_basic_net_choooser.insertItems()

    # BUTTONS CLICK
    def buttonClick(self):
        # GET BUTTON CLICKED
        btn = self.sender()
        btnName = btn.objectName()

        # 切换为基础模式界面
        if btnName == "btn_home":
            self.widgets.stackedWidget.setCurrentWidget(self.widgets.home_basic)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        # 切换为 Pro 模式界面
        if btnName == "btn_pro_switch":
            self.widgets.stackedWidget.setCurrentWidget(self.widgets.page_pro)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        # 设置界面
        if btnName == "btn_settings":
            self.widgets.stackedWidget.setCurrentWidget(self.widgets.page_settings)

        # 反馈界面
        if btnName == "btn_basic_feedback":
            self.widgets.stackedWidget.setCurrentWidget(self.widgets.page_feedback)
            self.widgets.btn_basic_feedback.setEnabled(False)

        # 识别垃圾类别按钮
        if btnName == "btn_basic_garbage_classification":
            # model_path = os.path.abspath('trained_models/resnet34.pth')
            # if self.widgets.checkBox_basic_default_model.isTristate() == True:
            #     model_path = os.path.abspath('trained_models/resnet34.pth')
            model_name = self.widgets.comboBox_basic_net_choooser.currentText()
            pm = self.widgets.basicpicturelabel.pixmap()
            size = pm.size()
            h = pm.width()
            w = pm.height()
            qimg = pm.toImage()
            bs = qimg.bits()
            # bs.setsize(h*w*4)
            img = np.frombuffer(bs, dtype=np.uint8).reshape((w, h, 4))
            # print(img.shape)
            # _thread.start_new_thread(AI_stuff.garbage_classification, (img, model_path, self.widgets))
            # data_to_send = {'task':'garbage_classification','reply_addr_port':('127.0.0.1',1024), 'arguements':()}
            for i in range(img.shape[0]):
                for j in range(img.shape[1]):
                    r = img[i][j][0]
                    b = img[i][j][2]
                    img[i][j][0] = b
                    img[i][j][2] = r
            ret = AI_stuff.garbage_classification(pic_np=img, model_name=model_name,
                                                  gpu=self.widgets.checkBox_GPU.isChecked(), widgets=self.widgets)

        # 批量识别
        if btnName == "btn_basic_batch_classification":
            pics_path = self.widgets.lineEdit_basic_dir_addr.text()
            pic_path_list = []
            os_walker = os.walk(pics_path)
            for path, dir_list, file_list in os_walker:
                for file_name in file_list:
                    pic_path_list.append(os.path.join(path) + '/' + file_name)
            _thread.start_new_thread(AI_stuff.batch_classification, (
            self.widgets, pic_path_list, self.widgets.comboBox_basic_net_choooser.currentText(),
            self.widgets.checkBox_GPU.isChecked()))

        # 选择图片按钮
        if btnName == 'btn_basic_choose_pic':
            _thread.start_new_thread(widgets_function.choose_picture, (self, self.widgets))

        # 裁剪图片按钮        
        if btnName == 'btn_basic_crop':
            _thread.start_new_thread(crop.cropui, (self, self.widgets))

        # 选择文件夹按钮
        if btnName == 'btn_basic_choose_dir':
            _thread.start_new_thread(widgets_function.msg, (self, self.widgets))

        # 打开模型文件按钮
        if btnName == 'btn_basic_choose_model':
            _thread.start_new_thread(AI_stuff.choose_default_Model, (self, self.widgets))

        # 选择数据集按钮
        # if btnName == 'btn_pro_choose_pic_2':
        #     _thread.start_new_thread(AI_stuff.choose_Picfile, (self, self.widgets))

        # 选择预训练模型按钮
        if btnName == 'btn_pro_choose_premodel':
            _thread.start_new_thread(AI_stuff.choose_Premodel, (self, self.widgets))

        if btnName == 'btn_page_feedback_submit':
            # _thread.start_new_thread(AI_stuff.choose_Premodel, (self, self.widgets))
            model_name = self.widgets.comboBox_basic_net_choooser.currentText()
            pm = self.widgets.basicpicturelabel.pixmap()
            size = pm.size()
            h = pm.width()
            w = pm.height()
            qimg = pm.toImage()
            bs = qimg.bits()
            # bs.setsize(h*w*4)
            img = np.frombuffer(bs, dtype=np.uint8).reshape((w, h, 4))
            for i in range(img.shape[0]):
                for j in range(img.shape[1]):
                    r = img[i][j][0]
                    b = img[i][j][2]
                    img[i][j][0] = b
                    img[i][j][2] = r
            self.widgets.stackedWidget.setCurrentWidget(self.widgets.home_basic)
            _thread.start_new_thread(AI_stuff.feedback_Optimizer, (
                img, int(self.widgets.comboBox_feedback.currentText().split(' ')[0]),
                self.widgets.comboBox_basic_net_choooser.currentText(), self.widgets.checkBox_GPU.isChecked(),
                self.widgets))

        # 训练
        if btnName == 'btn_pro_start_training':
            dataset = self.widgets.comboBox_pro_dataset_chooser_2.currentText()
            modelBasedOn = self.widgets.comboBox_pro_premodel_chooser.currentText()
            epoch = int(self.widgets.lineEdit_pro_epoch.text())
            batch_size = int(self.widgets.lineEdit_pro_batch.text())
            lr = float(self.widgets.lineEdit_pro_lr.text())
            epchtoSave = int(self.widgets.lineEdit_pro_saveevery_epoch.text())
            _thread.start_new_thread(AI_stuff.askServertoTrain,
                                     (dataset, modelBasedOn, self.widgets.checkBox_GPU.isChecked(), epoch, batch_size, lr, epchtoSave, self.widgets))

    # 点击checkbox
    def checkboxClick(self):
        cb = self.sender()
        cbName = cb.objectName()
        if cbName == 'checkBox_pro_pretrain':
            if cb.isChecked():
                self.widgets.btn_pro_choose_premodel.setEnabled(True)
                self.widgets.lineEdit_pro_choose_premodel.setEnabled(True)
            else:
                self.widgets.btn_pro_choose_premodel.setEnabled(False)
                self.widgets.lineEdit_pro_choose_premodel.setEnabled(False)

        if cbName == 'checkBox_basic_default_model':
            if cb.isChecked():
                self.widgets.comboBox_basic_net_choooser.setEnabled(False)
                self.widgets.comboBox_basic_net_choooser.setCurrentText(
                    self.widgets.comboBox_setting_default_net_choooser.currentText())
                # self.widgets.lineEdit_basic_model_addr.setEnabled(False)
                # self.widgets.btn_basic_choose_model.setEnabled(False)
            else:
                self.widgets.comboBox_basic_net_choooser.setEnabled(True)
                # self.widgets.lineEdit_basic_model_addr.setEnabled(True)
                # self.widgets.btn_basic_choose_model.setEnabled(True)

    def checkTrainingArguments(self):
        self.widgets.label.setText('')
        self.widgets.btn_pro_start_training.setEnabled(True)
        epch = self.widgets.lineEdit_pro_epoch.text()
        batch_size = self.widgets.lineEdit_pro_batch.text()
        saving_epch = self.widgets.lineEdit_pro_saveevery_epoch.text()
        lr = self.widgets.lineEdit_pro_lr.text()
        for integer in (epch, batch_size, saving_epch):
            try:
                a = int(integer)
                if a <= 0:
                    self.widgets.label.setText('请输入正确的训练参数')
                    self.widgets.btn_pro_start_training.setEnabled(False)
            except:
                self.widgets.label.setText('请输入正确的训练参数')
                self.widgets.btn_pro_start_training.setEnabled(False)
        try:
            a = float(lr)
            if a <= 0:
                self.widgets.label.setText('请输入正确的训练参数')
                self.widgets.btn_pro_start_training.setEnabled(False)
            if lr.replace('.', '') == lr:
                self.widgets.label.setText('请输入正确的训练参数')
                self.widgets.btn_pro_start_training.setEnabled(False)
        except:
            self.widgets.label.setText('请输入正确的训练参数')
            self.widgets.btn_pro_start_training.setEnabled(False)

    def comboChanged(self):
        cb = self.sender()
        cbName = cb.objectName()
        if cbName == 'comboBox_setting_default_net_choooser':
            self.widgets.comboBox_basic_net_choooser.setCurrentText(
                self.widgets.comboBox_setting_default_net_choooser.currentText())
            self.widgets.comboBox_pro_premodel_chooser.setCurrentText(
                self.widgets.comboBox_setting_default_net_choooser.currentText())

    # RESIZE EVENTS
    def resizeEvent(self, event):
        # Update Size Grips
        UIFunctions.resize_grips(self)

    # MOUSE CLICK EVENTS
    def mousePressEvent(self, event):  # ToDo: 检查这个 function 是否可以删去
        # SET DRAG POS WINDOW
        self.dragPos = event.globalPos()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("14-garbage-classification-icon.ico"))

    window = MainWindow()
    sys.exit(app.exec())

import time, json
import sys, os, platform, _thread
from modules import *  # Ui_MainWindow() imported
from widgets import *
import numpy as np
import pickle, client_sender
from PIL import Image

def readLocalIP():
    with open('local_ip.txt', mode='r') as ip:
        a = ip.read()
        return a

def readServerIP():
    with open('server_ip.txt', mode='r') as ip:
        a = ip.read()
        return a

def textBrowserAppender(txtBrowser, text=''):
    txtBrowser.insertHtml(
        '''
        <p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#3a534c;"><br>''' + text + '''</span></p>''')
    txtBrowser.moveCursor(QTextCursor.End)
    txtBrowser.moveCursor(QTextCursor.End)
    txtBrowser.moveCursor(QTextCursor.End)
    txtBrowser.moveCursor(QTextCursor.End)
    txtBrowser.moveCursor(QTextCursor.End)
    txtBrowser.moveCursor(QTextCursor.End)

def garbage_classification(pic_np=[], model_name='ResNet34', gpu=False, widgets=None):
    arguments = {'pic_np_list': pic_np, 'model_name': model_name, 'gpu': gpu}
    data = {'task': 'garbage_classification', 'receiver': [readLocalIP(), 11000], 'arguments': arguments}
    client_sender.send_to_server(serverPort=23333, data=pickle.dumps(data))
    textBrowserAppender(widgets.textBrowser_basic_log, text='<br>请求垃圾分类')


def choose_Picfile(self, widgets=None):
    directory = QFileDialog.getExistingDirectory(None, "选择文件夹", "/")
    widgets.lineEdit_pro__choose_dataset.setText(directory)


def choose_Premodel(self, widgets=None):
    modelName, modelType = QFileDialog.getOpenFileName(None, "选择预训练模型", "/", "*.pth")
    widgets.lineEdit_pro_choose_premodel.setText(modelName)


def choose_default_Model(self, widgets=None):
    modelName, modelType = QFileDialog.getOpenFileName(None, "选择模型文件", "/", "*.pth")
    widgets.lineEdit_basic_model_addr.setText(modelName)


def connectServer(widgets, host='127.0.0.1', port=23333):
    data = {'task': 'getDatasets', 'receiver': [readLocalIP(), 11000], 'arguments': None}
    textBrowserAppender(widgets.textBrowser_basic_log, '正在向服务器请求数据集列表')
    client_sender.send_to_server(serverPort=23333, data=pickle.dumps(data))
    data = {'task': 'getModelList', 'receiver': [readLocalIP(), 11000], 'arguments': None}
    textBrowserAppender(widgets.textBrowser_basic_log, '正在向服务器请求模型列表')
    client_sender.send_to_server(serverPort=23333, data=pickle.dumps(data))

def feedback_Optimizer(pic_np=[], correctionLabel = 0, model_name='ResNet34', gpu=False, widgets=None):
    arguments = {'pic_np': pic_np, 'correctionLabel': correctionLabel, 'model_name': model_name, 'gpu': gpu}
    data = {'task': 'feedback_Optimizer', 'receiver': [readLocalIP(), 11000], 'arguments': arguments}
    client_sender.send_to_server(serverPort=23333, data=pickle.dumps(data))

def askServertoTrain(dataset, modelBasedOn, gpu, epoch, batch_size, lr, epchtoSave, widgets):
    arguments = {'dataset':dataset,'modelBasedOn':modelBasedOn, 'gpu':gpu,'epoch':epoch,'batch_size':batch_size,'lr':lr,'epchtoSave':epchtoSave}
    data = {'task':'askServertoTrain','receiver': [readLocalIP(), 11000], 'arguments': arguments}
    client_sender.send_to_server(serverPort=23333, data=pickle.dumps(data))
    widgets.btn_pro_start_training.setEnabled(False)

def trainingPic(widgets, loss_list): #画training曲线图
    from PIL import Image, ImageQt
    # import numpy as np
    from moviepy.video.io.bindings import mplfig_to_npimage
    import matplotlib.pyplot as plt
    lens = len(loss_list)
    x_list=[]
    y_list=[]
    for i in range(lens):
        x_list.append(loss_list[i][0])
        y_list.append(loss_list[i][1])

    fig1 = plt.figure(figsize=(5,4)) #图片大小
    # plt.xlim(([0,lens]))
    # plt.ylim(([0,1]))
    plt.plot(x_list, y_list)
    plt.title("training_loss")
    plt.xlabel("iteration")
    plt.ylabel("loss")

    numpy_fig = mplfig_to_npimage(fig1).copy()
    b = Image.fromarray(numpy_fig, mode='RGB')
    #widgets.label_pro_pic.setPixmap(QPixmap.fromImage(ImageQt(b)))
    widgets.label_pro_pic.setPixmap(QPixmap.fromImage(ImageQt.toqimage(b)))

    plt.close()


def batch_classification(widgets, pic_path_list, model_name, gpu):
    pic_np_list = []
    for img_path in pic_path_list:
        try:
            img_np = np.array(Image.open(img_path).convert('RGB').resize((32, 32)))
        except:
            continue
        pic_np_list.append((os.path.basename(img_path), img_np))
    arguments = {'model_name':model_name, 'gpu': gpu, 'pic_np_list':pic_np_list}
    data = {'task': 'batch_classification', 'receiver': [readLocalIP(), 11000], 'arguments': arguments}
    client_sender.send_to_server(serverPort=23333, data=pickle.dumps(data))

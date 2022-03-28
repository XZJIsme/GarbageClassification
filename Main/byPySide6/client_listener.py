import _thread
import json
from socket import *
import pickle

import AI_stuff


def client_listener(widgets, serverName = '', serverPort = 11000):
    host = ''
    port = serverPort
    ADDR = (host, port)
    BUFSIZ = 1024

    tcpSocket = socket(AF_INET, SOCK_STREAM)
    tcpSocket.bind(ADDR)
    # set the max number of tcp connection
    tcpSocket.listen(1)

    while True:
        print('client waiting for connection...')
        clientSocket, clientAddr = tcpSocket.accept()
        print('client conneted form: %s' % clientAddr[0])

        data = []
        while True:
            try:
                data_ = clientSocket.recv(BUFSIZ)
                if not data_: break
                # print('recieved')
                data.append(data_)
                pass
            except IOError as e:
                print(e)
                clientSocket.close()
                break
            if not data:
                break

        data = pickle.loads(b''.join(data))
        # 处理收到的 data
        # data = pickle.loads(data)
        # if data['task'] == 'garbage_classification':
        #     print(data)
        if data['task'] == 'gotModelList':
            widgets.comboBox_basic_net_choooser.insertItems(0, data['got'])
            widgets.comboBox_setting_default_net_choooser.insertItems(0, data['got'])
            widgets.comboBox_pro_premodel_chooser.insertItems(0, data['got'])
            msg = '<br>已从服务器获取 '+str(len(data['got']))+' 个模型 ID'
            AI_stuff.textBrowserAppender(widgets.textBrowser_basic_log, msg)
            print(data)
            pass

        if data['task'] == 'gotDatasets':
            widgets.comboBox_pro_dataset_chooser_2.insertItems(0, data['got'])
            msg = '<br>已从服务器获取 '+str(len(data['got']))+' 个数据集'
            AI_stuff.textBrowserAppender(widgets.textBrowser_basic_log, msg)
            print(data)
            pass

        if data['task'] == 'gotClassRes':
            msg = '<br>已从服务器获取'+'垃圾分类结果'
            AI_stuff.textBrowserAppender(widgets.textBrowser_basic_log, msg)
            i=data['got']
            dic = open('垃圾数据字典.json', mode='r', encoding='utf-8').read()
            dic = json.loads(dic)
            n = dic['garbage'][str(i)]['name']
            c = dic['garbage'][str(i)]['classification']
            c = dic['classification'][str(c)]
            widgets.label_basic_classification_result_2.setText(n+', '+c)
            # print(data)
            widgets.btn_basic_feedback.setEnabled(True)
            widgets.label_3.setStyleSheet('background-image: url(:/images/images/images/'+c+'.png);')
            pass

        if data['task'] == 'serverGotFeedback':
            msg = '<br>服务器已经收到反馈，识别模型已修正'
            AI_stuff.textBrowserAppender(widgets.textBrowser_basic_log, msg)
            pass

        if data['task'] == '训练完成':
            msg = '<br>训练已完成'
            AI_stuff.textBrowserAppender(widgets.textBrowser_basic_log, msg)
            widgets.btn_pro_start_training.setEnabled(True)
            pass

        if data['task'] == 'updateTrainingGraph':
            print(data['got'])
            _thread.start_new_thread(AI_stuff.trainingPic,(widgets, data['got']))

        if data['task'] == 'got_batch_classification':
            ans_list = data['got']
            print(ans_list)
            msg = '<br>批量识别结果'
            for ans in ans_list:
                i = int(ans[1])
                dic = open('垃圾数据字典.json', mode='r', encoding='utf-8').read()
                dic = json.loads(dic)
                n = dic['garbage'][str(i)]['name']
                c = dic['garbage'][str(i)]['classification']
                c = dic['classification'][str(c)]
                msg+=n+', '
                msg+=c+', '+ans[0]+'<br>'
            AI_stuff.textBrowserAppender(txtBrowser=widgets.textBrowser_basic_log, text=msg)

        # returnData = '这里是发送回去的值'
        # clientSocket.send(returnData.encode('utf-8'))
        clientSocket.close()
        print('server接收一次完毕，等待下一次接收')
    tcpSocket.close()


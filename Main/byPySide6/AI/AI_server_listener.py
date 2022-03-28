import pickle
from socket import *
from PIL import Image
import numpy as np
import torch
import _thread

import AI_server_sender, db_get, AI_model

host = ''
port = 23333
ADDR = (host, port)
BUFSIZ = 1024

tcpSocket = socket(AF_INET, SOCK_STREAM)
tcpSocket.bind(ADDR)
# set the max number of tcp connection
tcpSocket.listen(1)

def newTraining(data):
    arguments = data['arguments']
    dataset=arguments['dataset']
    modelBasedOn=arguments['modelBasedOn']
    gpu=arguments['gpu']
    epoch=arguments['epoch']
    batch_size=arguments['batch_size']
    lr=arguments['lr']
    epchtoSave=arguments['epchtoSave']
    modelTrainer = AI_model.Model_with_Trainer(model_name=modelBasedOn)
    model_address = db_get.getModelAddr(modelBasedOn)
    modelTrainer.load_model(model_address)
    modelTrainer.gpu_switch(gpu)
    pic_label_pairs = db_get.getPicsWithLabelsFromParticularDataset(dataset)
    modelTrainer.train_with_sender(batch_size, epoch, 0.85, pic_label_pairs, lr, epchtoSave, data)
    ret = {'task': '训练完成', 'got': None}
    AI_server_sender.send_back(serverName=data['receiver'][0], serverPort=data['receiver'][1],
                                   data=pickle.dumps(ret))

while True:
    print('waiting for connection...')
    clientSocket, clientAddr = tcpSocket.accept()
    print('conneted form: %s' % clientAddr[0])

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
    if data['task'] == 'garbage_classification':
        arguments = data['arguments']
        pic_np = arguments['pic_np_list']
        model_name = arguments['model_name']
        gpu = arguments['gpu']
        model_address = db_get.getModelAddr(model_name)
        model = AI_model.Model_with_Trainer(model_name=model_name)
        model.load_model(model_file_path=model_address)
        model.gpu_switch(gpu)
        # model.forward_single_pic(pic_np)
        ret = {'task': 'gotClassRes', 'got': int(model.forward_single_pic(pic_np))}
        AI_server_sender.send_back(serverName=data['receiver'][0], serverPort=data['receiver'][1],
                                   data=pickle.dumps(ret))

    elif data['task'] == 'getDatasets':
        ret_list = db_get.getDatasets()
        ret = {'task': 'gotDatasets', 'got': ret_list}
        AI_server_sender.send_back(serverName=data['receiver'][0], serverPort=data['receiver'][1],
                                   data=pickle.dumps(ret))
    elif data['task'] == 'getModelList':
        ret_list = db_get.getModelList()
        ret = {'task': 'gotModelList', 'got': ret_list}
        AI_server_sender.send_back(serverName=data['receiver'][0], serverPort=data['receiver'][1],
                                   data=pickle.dumps(ret))
    elif data['task'] == 'feedback_Optimizer':
        arguments = data['arguments']
        pic_np = arguments['pic_np']
        correctionLabel = arguments['correctionLabel']
        model_name = arguments['model_name']
        gpu = arguments['gpu']
        model_address = db_get.getModelAddr(model_name)
        model = AI_model.Model_with_Trainer(model_name=model_name)
        model.load_model(model_file_path=model_address)
        model.gpu_switch(gpu)
        while int(model.forward_single_pic(pic_np)) != correctionLabel:
            img = pic_np
            if img.shape[2] == 4:
                img = Image.fromarray(img, mode='RGBA').convert('RGB')
            else:
                img = Image.fromarray(img, mode='RGB')
            img = np.array(img.resize((32, 32)))
            reshape_tuple = (img.shape[2], img.shape[1], img.shape[0])
            img_tensor = torch.tensor([np.array(img).reshape(reshape_tuple).tolist()], dtype=torch.float)
            if model.gpu:
                img_tensor = img_tensor.cuda()
            out = model.model(img_tensor)
            label_encode = torch.zeros_like(out)
            label_encode[0][correctionLabel] = 1
            loss = model.loss_f(out, label_encode)
            optimizer = torch.optim.Adam(model.model.parameters(), lr=0.00001)
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()
        ret = {'task': 'serverGotFeedback', 'got': None}
        torch.save(model.model, model_address)
        print('新模型已保存')
        AI_server_sender.send_back(serverName=data['receiver'][0], serverPort=data['receiver'][1],
                                   data=pickle.dumps(ret))
    elif data['task'] == 'askServertoTrain':
        arguments = data['arguments']
        _thread.start_new_thread(newTraining,(data,))

    elif data['task'] == 'batch_classification':
        arguments = data['arguments']
        model_name = arguments['model_name']
        gpu = arguments['gpu']
        pic_np_list = arguments['pic_np_list']
        model_address = db_get.getModelAddr(model_name)
        model = AI_model.Model_with_Trainer(model_name=model_name)
        model.load_model(model_file_path=model_address)
        model.gpu_switch(gpu)
        ans_list = []
        for p in pic_np_list:
            ans_list.append((p[0], int(model.forward_single_pic(p[1]))))
        ret = {'task': 'got_batch_classification', 'got': ans_list}
        AI_server_sender.send_back(serverName=data['receiver'][0], serverPort=data['receiver'][1],
                                   data=pickle.dumps(ret))


    returnData = '这里是发送回去的值'
    clientSocket.send(returnData.encode('utf-8'))
    clientSocket.close()
    print('server接收一次完毕，等待下一次接收')
tcpSocket.close()

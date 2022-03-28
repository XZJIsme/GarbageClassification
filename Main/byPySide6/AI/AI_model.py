import pickle

import torchvision, torch, os, random, math
import torch.utils.data
from PIL import Image
import numpy as np

# import AI_server_sender, db_get
import AI_server_sender, db_get


def dataset_reader(dataset_dir):
    try:
        list_ret = []
        for i in range(0, 40):  # 四十个垃圾分类
            os_walker = os.walk(os.path.join(dataset_dir, str(i)))
            for path, dir_list, file_list in os_walker:
                for file_name in file_list:
                    list_ret.append((os.path.join(path) + '/' + file_name, i))
        random.shuffle(list_ret)
        return list_ret
    except:
        print('dataset_reader_error')


class DatasetGarbageClassification(torch.utils.data.Dataset):
    def __init__(self, pic_label_pairs, begin=0, size=0):
        self.pic_label_pairs = pic_label_pairs[begin:begin + size]
        self.size = size

    def __getitem__(self, idx):
        img_path = self.pic_label_pairs[idx][0]
        img_np = np.array(Image.open(img_path).convert('RGB').resize((32, 32)))
        reshape_tuple = (img_np.shape[2], img_np.shape[1], img_np.shape[0])
        img_tensor = torch.tensor(np.array(img_np).reshape(reshape_tuple).tolist(), dtype=torch.float)
        return img_tensor, self.pic_label_pairs[idx][1]  # ToDo: 此处默认使用 cuda 了
        # except:
        #     return 'fuck'

    def __len__(self):
        return len(self.pic_label_pairs)


class Model_with_Trainer:
    def __init__(self, model_name='ResNet34', loss_f='CrossEntropyLoss'):
        self.model_name = ''
        self.model_addr=db_get.getModelAddr(model_name)
        if model_name == 'ResNet34':
            self.model_name = 'ResNet34'
            self.loss_f = None
            # self.model = torchvision.models.resnet152(pretrained=True)
            self.model = torchvision.models.resnet34()
            self.model.fc = torch.nn.Linear(self.model.fc.in_features, 40)
            self.gpu = False
            if loss_f == 'CrossEntropyLoss':
                self.loss_f = torch.nn.CrossEntropyLoss()
        if model_name == 'ResNet50':
            self.model_name = 'ResNet50'
            self.loss_f = None
            # self.model = torchvision.models.resnet152(pretrained=True)
            self.model = torchvision.models.resnet50()
            self.model.fc = torch.nn.Linear(self.model.fc.in_features, 40)
            self.gpu = False
            if loss_f == 'CrossEntropyLoss':
                self.loss_f = torch.nn.CrossEntropyLoss()

    def gpu_switch(self, switch=False):
        if switch == True:
            try:
                self.gpu = True
                self.model.cuda()
            except:
                self.gpu = False
        if switch == False or self.gpu == False:
            self.gpu=False
            self.model.cpu()

    def train(self, batch_size=1500, epoch=1000, train_size=0.995, pic_label_pairs=None, lr=0.0001):
        train_size = math.floor(train_size * len(pic_label_pairs))
        train_dataset = DatasetGarbageClassification(pic_label_pairs, begin=0, size=train_size)
        test_dataset = DatasetGarbageClassification(pic_label_pairs, begin=train_size,
                                                    size=(len(pic_label_pairs) - train_size))
        train_loader = torch.utils.data.DataLoader(train_dataset, batch_size=batch_size, shuffle=True)
        test_loader = torch.utils.data.DataLoader(test_dataset, batch_size=batch_size, shuffle=False)
        optimizer = torch.optim.Adam(self.model.parameters(), lr=lr)
        # optimizer = torch.optim.SGD(self.model.parameters(), lr=lr)
        loss = None
        i_=0
        for epc in range(epoch):
            self.model.train()
            for data in train_loader:
                i_+=1
                img_tensor, label = data
                if self.gpu:
                    img_tensor = img_tensor.cuda()
                out = self.model(img_tensor)
                label_encode = torch.zeros_like(out)
                for i in range(len(label)):
                    try:
                        if len(label_encode.shape)!=2:
                            pass
                        label_encode[i][label[i]]=1
                    except:
                        pass
                if self.gpu:
                    label_encode = label_encode.cuda()
                # label_encode[0][label - 1] = 1
                loss = self.loss_f(out, label_encode)
                optimizer.zero_grad()
                loss.backward()
                optimizer.step()
                # print(loss.data.item())
            print('epoch=',epc, loss.data.item())
            self.model.eval()
            c_ = 0
            s_ = 0
            for data in test_loader:
                img_tensor, label = data
                if self.gpu:
                    img_tensor = img_tensor.cuda()
                out = self.model(img_tensor)
                label_encode = torch.zeros_like(out)
                for i in range(len(label)):
                    try:
                        if len(label_encode.shape) != 2:
                            pass
                        label_encode[i][label[i]] = 1
                    except:
                        pass
                c_ += (torch.nn.Softmax(dim=1)(out).argmax(1) == label_encode.argmax(1)).sum()
                s_ += label_encode.shape[0]
            print('epoch acc:', c_/s_)
            c_ = 0
            s_ = 0
            for data in train_loader:
                img_tensor, label = data
                if self.gpu:
                    img_tensor = img_tensor.cuda()
                out = self.model(img_tensor)
                label_encode = torch.zeros_like(out)
                for i in range(len(label)):
                    try:
                        if len(label_encode.shape) != 2:
                            pass
                        label_encode[i][label[i]] = 1
                    except:
                        pass
                c_ += (torch.nn.Softmax(dim=1)(out).argmax(1) == label_encode.argmax(1)).sum()
                s_ += label_encode.shape[0]
            print('epoch acc:', c_ / s_)
            if(epc%50==0):
                pass
        pass

    def train_with_sender(self, batch_size=1500, epoch=1000, train_size=0.995, pic_label_pairs=None, lr=0.0001, epchtoSave=1, data1=None):
        train_size = math.floor(train_size * len(pic_label_pairs))
        train_dataset = DatasetGarbageClassification(pic_label_pairs, begin=0, size=train_size)
        test_dataset = DatasetGarbageClassification(pic_label_pairs, begin=train_size,
                                                    size=(len(pic_label_pairs) - train_size))
        train_loader = torch.utils.data.DataLoader(train_dataset, batch_size=batch_size, shuffle=True)
        test_loader = torch.utils.data.DataLoader(test_dataset, batch_size=batch_size, shuffle=False)
        optimizer = torch.optim.Adam(self.model.parameters(), lr=lr)
        # optimizer = torch.optim.SGD(self.model.parameters(), lr=lr)
        loss = None
        i_=0
        i_loss_list = []
        for epc in range(epoch):
            self.model.train()
            for data in train_loader:
                # print('1111111')/
                i_+=1
                img_tensor, label = data
                if self.gpu:
                    img_tensor = img_tensor.cuda()
                out = self.model(img_tensor)
                label_encode = torch.zeros_like(out)
                for i in range(len(label)):
                    # try:
                    if len(label_encode.shape)!=2:
                        pass
                    label_encode[i][label[i]]=1
                    # except:
                    #     pass
                if self.gpu:
                    label_encode = label_encode.cuda()
                # label_encode[0][label - 1] = 1
                loss = self.loss_f(out, label_encode)
                optimizer.zero_grad()
                loss.backward()
                optimizer.step()
                # print(loss.data.item())
                if i_ % 1 == 0:
                    print(loss.data.item())
                    i_loss_list.append((i_, loss.data.item()))
                    ret = {'task': 'updateTrainingGraph', 'got': i_loss_list}
                    AI_server_sender.send_back(serverName=data1['receiver'][0], serverPort=data1['receiver'][1], data=pickle.dumps(ret))
            print('epoch=',epc, loss.data.item())
            if (epoch%epchtoSave==0 or epoch>epchtoSave):
                self.model.cpu()
                self.model.eval()
                torch.save(self.model, self.model_addr)
                if self.gpu:
                    self.model.cuda()
                self.model.train()
            self.model.eval()
            c_ = 0
            s_ = 0
            for data in test_loader:
                img_tensor, label = data
                if self.gpu:
                    img_tensor = img_tensor.cuda()
                out = self.model(img_tensor)
                label_encode = torch.zeros_like(out)
                for i in range(len(label)):
                    try:
                        if len(label_encode.shape) != 2:
                            pass
                        label_encode[i][label[i]] = 1
                    except:
                        pass
                c_ += (torch.nn.Softmax(dim=1)(out).argmax(1) == label_encode.argmax(1)).sum()
                s_ += label_encode.shape[0]
            print('epoch acc:', c_/s_)
            c_ = 0
            s_ = 0
            for data in train_loader:
                img_tensor, label = data
                if self.gpu:
                    img_tensor = img_tensor.cuda()
                out = self.model(img_tensor)
                label_encode = torch.zeros_like(out)
                for i in range(len(label)):
                    try:
                        if len(label_encode.shape) != 2:
                            pass
                        label_encode[i][label[i]] = 1
                    except:
                        pass
                c_ += (torch.nn.Softmax(dim=1)(out).argmax(1) == label_encode.argmax(1)).sum()
                s_ += label_encode.shape[0]
            print('epoch acc:', c_ / s_)
            if(epc%50==0):
                pass
        pass


    def load_model(self, model_file_path=''):
        self.model = torch.load(model_file_path)
        self.model_addr = model_file_path

    def forward_single_pic(self, img):
        if img.shape[2]==4:
            img = Image.fromarray(img, mode='RGBA').convert('RGB')
        else:
            img = Image.fromarray(img, mode='RGB')
        img = np.array(img.resize((32, 32)))
        reshape_tuple = (img.shape[2], img.shape[1], img.shape[0])
        img_tensor = torch.tensor([np.array(img).reshape(reshape_tuple).tolist()], dtype=torch.float)
        if self.gpu:
            return torch.nn.Softmax(dim=1)(self.model(img_tensor.cuda())).argmax()
        else:
            return torch.nn.Softmax(dim=1)(self.model(img_tensor.cpu())).argmax()


if __name__ == '__main__':
    trainer = Model_with_Trainer()
    trainer.gpu_switch(switch=True)
    pic_label_pairs=dataset_reader(dataset_dir='./这是老师给的数据集/imagenet')
    pic_label_pairs=pic_label_pairs
    trainer.train_with_sender(batch_size=32,pic_label_pairs=pic_label_pairs)

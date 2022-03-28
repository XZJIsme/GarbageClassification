#!/usr/bin/python
import os
import random
import sqlite3

conn = sqlite3.connect('AI.db')
c = conn.cursor()

c.execute('''
   create TABLE IF NOT EXISTS MODELS
   (MODEL_NAME TEXT PRIMARY KEY NOT NULL,
   MODEL_ADDRESS TEXT NOT NULL
   );
''')
c.execute('''
    INSERT INTO MODELS
    VALUES ('ResNet34', 'trained_models/resnet34.pth');
''')
c.execute('''
    INSERT INTO MODELS
    VALUES ('ResNet50', 'trained_models/resnet50.pth');
''')

c.execute('''
   create TABLE IF NOT EXISTS DATASETS
   (DATASET_NAME TEXT PRIMARY KEY NOT NULL
   );
''')
c.execute('''
    INSERT INTO DATASETS
    VALUES ('ImageNet_garbage_classification');
''')

c.execute('''
   create TABLE IF NOT EXISTS PICTURES
   (PICTURE_ADDRESS TEXT PRIMARY KEY NOT NULL,
   DATASET_NAME TEXT NOT NULL,
   LABEL TEXT NOT NULL
   );
''')


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


pic_list = dataset_reader(dataset_dir='这是老师给的数据集\\imagenet')
for pic in pic_list:
    pic_addr = pic[0]
    pic_label = str(pic[1])
    sql = "INSERT INTO PICTURES VALUES ('" + pic_addr + "','" + "ImageNet_garbage_classification" + "','" + pic_label + "');"
    c.execute(sql)

conn.commit()
conn.close()

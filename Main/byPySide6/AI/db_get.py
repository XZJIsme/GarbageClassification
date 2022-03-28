import os
import random
import sqlite3

def getDatasets():
    conn = sqlite3.connect('AI.db')
    c = conn.cursor()
    dataset_list = []
    cursor = c.execute("SELECT *  from DATASETS")
    for row in cursor:
        dataset_list.append(row[0])
    conn.close()
    return dataset_list

def getModelList():
    conn = sqlite3.connect('AI.db')
    c = conn.cursor()
    model_name_list = []
    cursor = c.execute("SELECT MODEL_NAME from MODELS")
    for row in cursor:
        model_name_list.append(row[0])
    conn.close()
    return model_name_list

def getModelAddr(model_name='ResNet34'):
    conn = sqlite3.connect('AI.db')
    c = conn.cursor()
    ret = None
    cursor = c.execute("SELECT MODEL_ADDRESS  from MODELS WHERE MODELS.MODEL_NAME IS '" + model_name + "'")
    for row in cursor:
        ret = row[0]
    conn.close()
    return ret

def getPicsWithLabelsFromParticularDataset(dataset_name='ImageNet_garbage_classification'):
    conn = sqlite3.connect('AI.db')
    c = conn.cursor()
    ret = []
    cursor = c.execute("SELECT PICTURE_ADDRESS, LABEL from PICTURES WHERE DATASET_NAME IS '" + dataset_name + "'")
    for row in cursor:
        ret.append((row[0], int(row[1])))
    conn.close()
    return ret

pass

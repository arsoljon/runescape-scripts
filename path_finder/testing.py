import tensorflow as tf
from tensorflow import keras
import numpy as np
import matplotlib.pyplot as plt
import sklearn.datasets
from PIL import Image
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder
import json, sys, os
np.set_printoptions(threshold=sys.maxsize)


cwd = os.getcwd()
save_data_path = "{}/data/image_data.json".format(cwd)
train_data_dir = "{}/{}".format(cwd, "data/mine/Train")
validation_data_dir = "{}/{}".format(cwd, "data/mine/Test")
nb_train_samples = 33
nb_validation_samples = 16
class_samples = ["fishing", "mining"]

def getSampleData(data_sample_dir, sample_length):
    data = []
    for c in class_samples:
        current_dir = "{}/{}".format(data_sample_dir, c)
        for j in range(sample_length):
            pic_path = "{}/{}.jpg".format(current_dir, j)
            img = Image.open(pic_path)
            img = img.convert('RGB')
            imgRGB = []
            for x in range(img.width):
                for y in range(img.height):
                    r,g,b = img.getpixel((x, y))
                    rgb = [r,g,b]
                    imgRGB.append(rgb)
            data.append(imgRGB)
    return np.array(data)

def getYData(sample_length):
    data = []
    for i in range(len(class_samples)):
        for j in range(sample_length):
            data.append(class_samples[i])
    data = np.array(data)
    label = LabelEncoder()
    int_data = label.fit_transform(data)
    int_data = int_data.reshape(len(int_data),1)

    onehot_data = OneHotEncoder(sparse=False)
    onehot_data = onehot_data.fit_transform(int_data)
    return (onehot_data)
    



def save_data(tn_x, tn_y, ts_x, ts_y):
    if(os.path.exists(save_data_path) == False):
        fp = open(save_data_path, 'x')
        fp.close()
    with open(save_data_path, 'w', encoding="utf-8") as f:
        data = {"train_x" : str(tn_x), "train_y" : str(tn_y), "test_x" : str(ts_x), "test_y" : str(ts_y)}
        json.dump(data, f)

       
def get_data():
    data = {}
    try: 
        with open(save_data_path, 'r', encoding="utf-8") as f:
            data = json.loads(f.read()) 
    except:
        print("unable to open file")
    return (np.array(data["train_x"]), np.array(data["train_y"]), np.array(data["test_x"]), np.array(data["test_y"]))




def prompt():
    train_x = getSampleData(train_data_dir, nb_train_samples)
    test_x = getSampleData(validation_data_dir, nb_validation_samples)
    train_y = getYData(nb_train_samples)
    test_y = getYData(nb_validation_samples)
    print("RESULT : {}".format(len(train_x)))
    print("RESULT : {}".format(len(test_x)))
    print("RESULT : {}".format(len(train_y)))
    print("RESULT : {}".format(len(test_y)))
    save_data(train_x, train_y, test_x, test_y)
    train_x, train_y, test_x, test_y = get_data()
    print("RESULT : {}".format(len(train_x)))
    print("RESULT : {}".format(len(test_x)))
    print("RESULT : {}".format(len(train_y)))
    print("RESULT : {}".format(len(test_y)))


prompt()
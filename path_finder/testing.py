#pre process data then determine binary vs multi class classification

import tensorflow as tf
from tensorflow import keras
import numpy as np
import matplotlib.pyplot as plt
import sklearn.datasets
from PIL import Image
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder
import json, sys, os
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report, confusion_matrix
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

    X = np.append(train_x,test_x, axis=0)
    y = np.append(train_y, test_y, axis=0)

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20) 
    scaler = StandardScaler()
    scaler.fit(X_train)
    X_train = scaler.transform(X_train)
    X_test = scaler.transform(X_test) 
    classifier = KNeighborsClassifier(n_neighbors=5)
    classifier.fit(X_train, y_train) 
    y_predict = classifier.predict(X_test)
    print(confusion_matrix(y_test, y_predict))
    print(classification_report(y_test, y_predict))
    print("RESULT : {}".format(len(X)))
    print("RESULT : {}".format(len(y)))

    print("RESULT : {}".format(len(X_train)))
    print("RESULT : {}".format(len(X_test)))
    print("RESULT : {}".format(len(y_train)))
    print("RESULT : {}".format(len(y_test)))
    save_data(train_x, train_y, test_x, test_y)
    train_x, train_y, test_x, test_y = get_data()
    print("RESULT : {}".format(len(train_x)))
    print("RESULT : {}".format(len(test_x)))
    print("RESULT : {}".format(len(train_y)))
    print("RESULT : {}".format(len(test_y)))


prompt()
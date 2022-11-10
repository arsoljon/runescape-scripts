import tensorflow as tf
from tensorflow import keras
import numpy as np
import matplotlib.pyplot as plt
import os
import sklearn.datasets
from PIL import Image
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder

cwd = os.getcwd()
train_data_dir = "{}/{}".format(cwd, "data/mine/Train")
validation_data_dir = "{}/{}".format(cwd, "data/mine/Test")
nb_train_samples = 33
nb_validation_samples = 16
class_samples = ["fishing", "mining"]

def getSampleData(data_dir, sample_length):
    data = []
    for c in class_samples:
        current_dir = "{}/{}".format(data_dir, c)
        new_class = []
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
        new_class = []
        for j in range(sample_length):
            data.append(class_samples[i])
    data = np.array(data)
    label = LabelEncoder()
    int_data = label.fit_transform(data)
    int_data = int_data.reshape(len(int_data),1)

    onehot_data = OneHotEncoder(sparse=False)
    onehot_data = onehot_data.fit_transform(int_data)
    return (onehot_data)
    

train_x = getSampleData(train_data_dir, nb_train_samples)
test_x = getSampleData(validation_data_dir, nb_validation_samples)

print("RESULT : {}".format(len(train_x)))
print("RESULT : {}".format(len(test_x)))

train_y = getYData(nb_train_samples)
test_y = getYData(nb_validation_samples)

print("RESULT : {}".format(train_y.shape))
print("RESULT : {}".format(test_y.shape))







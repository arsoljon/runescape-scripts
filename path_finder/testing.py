import tensorflow as tf
from tensorflow import keras
import numpy as np
import matplotlib.pyplot as plt
import os
import sklearn.datasets
from PIL import Image

cwd = os.getcwd()
train_data_dir = "{}/{}".format(cwd, "data/mine/Train")
validation_data_dir = "{}/{}".format(cwd, "data/mine/Test")
nb_train_samples = 33
nb_validation_samples = 16

def getSampleData(data_dir, sample_length):
    data = []
    class_samples = ["fishing", "mining"]
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
            new_class.append(imgRGB)
        data.append(new_class)
    return data

train = getSampleData(train_data_dir, nb_train_samples)
test = getSampleData(validation_data_dir, nb_validation_samples)
print("RESULT : {}".format(len(train[0])))
print("RESULT : {}".format(len(test[0])))

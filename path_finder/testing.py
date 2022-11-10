import tensorflow as tf
from tensorflow import keras
import numpy as np
import matplotlib.pyplot as plt
import os
import sklearn.datasets
from PIL import Image

img_width, img_height = 10, 10


cwd = os.getcwd()
train_data_dir = "{}/{}".format(cwd, "data/mine/Train")
validation_data_dir = "{}/{}".format(cwd, "data/mine/Test")
path = "{}/{}".format(cwd, "data/mine/Train/mining/1.jpg")
#data = sklearn.datasets.load_files(path, shuffle='False')
img = Image.open(path)
img = img.convert('RGB')
r,g,b = img.getpixel((1,1))



nb_train_samples = 33
nb_validation_samples = 16

epochs = 1
batch_size = 1


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
fashion_mnist = keras.datasets.fashion_mnist
(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()

print(train_images.shape)
print(train_labels.shape)
print(test_images.shape)
print(test_images.shape)
print(r," " , b, " ", g)
class_names = ['T-shirt/top', 'Sneaker', 'Pullover', 'Ankle boot', 'Coat', 'Sandal', 'Shirt', 'Trouser', 'Bag', 'Dress']

plt.figure()
plt.imshow(train_images[0])
plt.colorbar()
plt.grid(False)
plt.show()
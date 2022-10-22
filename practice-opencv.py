from re import sub
from tkinter import W
import cv2
import numpy as np

dir_name = "./clicker-pics/"
file_name = "pre-full.png"
path = dir_name + file_name

image = cv2.imread(path)


height, width = image.shape[:2]
print(f"Height={height}, Width={width}")

def otherFunctions():
    (B,G,R) = image[100,100]

    print(f"R={R}, G={G}, B={B}")

    B = image[100,100,0]
    roi = image[100 : 500, 200 : 700]

    resize = cv2.resize(image, (800,800))
    ratio = 800/width
    dim = (800, int(height * ratio))
    resize_aspect = cv2.resize(image, dim)

    center = (width // 2, height // 2)
    matrix = cv2.getRotationMatrix2D(center, -45, 1.0)
    rotated = cv2.warpAffine(image,matrix,(width, height))

def createGrid():
    allCoords = []
    xcount = 0
    xmax = 4
    ymax = 7
    output = image.copy()
    for i in range(ymax):
        xcount = 0
        for j in range(xmax):
            x = int (xcount * (width/xmax))
            y = int (i * (height/ymax))
            coord1 = [x, y]
            xcount += 1
            x = int (xcount * (width/xmax))
            y = int ((i + 1 ) * (height/ymax))
            coord2 = [x,y]
            rectangle = cv2.rectangle(output, (coord1[0],coord1[1]), (coord2[0], coord2[1]), (255, 0, 0), 1)
            output = rectangle.copy()
            allCoords.append([coord1, coord2])
    cv2.imshow('image', rectangle)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return allCoords

if __name__ == "__main__":
    allCoords = createGrid()
    #print(allCoords)
    count = [0, 0, 0]
    items = []
    for k in range(20):
        subsectionCoordinates = allCoords[k]
        x_min, y_min = subsectionCoordinates[0]
        x_max, y_max = subsectionCoordinates[1]
        item = []
        for i in range(y_min + 1, y_max):
            for j in range(x_min + 1, x_max):
                image[i, j] = [0,0,0]
                item.append(image[i, j])
                count += image[j, i]
        items.append(item)
    pixel = image[1,1]
    pixel2 = image[2,2]
    pixeltotal = pixel + pixel
    print(pixel)
    print(image[0][0] + pixel)
    print(image[1][1] + image[0][0])
    print(image[0][0].shape)
    test1 = np.array([1,2,3,4,5,6])
    test2 = [4,5,6,1,2]
    print(len(items[3]))
    createGrid()
    
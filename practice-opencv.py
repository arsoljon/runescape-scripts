from tkinter import W
import cv2

dir_name = "./clicker-pics/"
file_name = "pre-full.png"
path = dir_name + file_name

image = cv2.imread(path)


height, width = image.shape[:2]

print(f"Height={height}, Width={width}")

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
    cv2.imshow('image', rectangle)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    createGrid()
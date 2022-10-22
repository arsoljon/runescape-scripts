from tkinter import W
import cv2

dir_name = './clicker-pics/'
file_name = 'pre-full.png'

image = cv2.imread(dir_name+file_name)

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

output = image.copy()
rectangle = cv2.rectangle(output, (1500,900), (600, 400), (255, 0, 0), 2)

output = image.copy()
text = cv2.putText(output, 'OpenCV Demo', (500,550),cv2.FONT_HERSHEY_SIMPLEX, 4, (255,0,0),2)
if __name__ == "__main__":
    pass
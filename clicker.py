##Goal: Inconspicuously click on the screen to repeat mundane clicking. 
#   will screenshot section of the screen that displays the inventory, 
#   than compare the before and after to check if inventory changed. 
#   if not then end program. 

#time: 1:14, 1:20
#left off on converting images into a simpler black and white image. 
# so it is easier to calculate binary values from image. 
# need to compare binary values to check if there is a change to decide to click again.  

from operator import inv
import pyautogui, time, random, winsound, pyscreenshot, cv2
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import cvlib as cv
from cvlib.object_detection import draw_bbox
from numpy.lib.polynomial import poly

file_name = "./clicker-pics"
inventoryCoord = []
oreCoord = []

def getPosition(name):
    #set ore or inventory coordinates by prompting location. 
    index = 0
    coords = []
    global inventoryCoord, oreCoord
    while index < 4:
        buffer = 3 
        while buffer >= 1: 
            print(f"{buffer}...")
            buffer -= 1
            time.sleep(1)
        currentLocation = pyautogui.position()
        #append location to list of coordinates. 
        coords.append(currentLocation)
        index += 1
    #take lowest and highest x1, y1, x2, y2 values and put them in a list; 
    # [x1Min, y1Min, x2Max, y2Max] 
    x1 = min(coords[0][0], coords[1][0], coords[2][0], coords[3][0])
    y1 = min(coords[0][1], coords[1][1], coords[2][1], coords[3][1])
    x2 = max(coords[0][0], coords[1][0], coords[2][0], coords[3][0])
    y2 = max(coords[0][1], coords[1][1], coords[2][1], coords[3][1])
    someList = [x1, y1, x2, y2]
    if(name == "inventory"):
        inventoryCoord = someList
    else:
        oreCoord = someList
    print(f"done: {someList}")
        

def funcBrightContrast(bright=0):
    bright = cv2.getTrackbarPos('bright', 'Life2Coding')
    contrast = cv2.getTrackbarPos('contrast', 'Life2Coding')
    effect = apply_brightness_contrast(img,bright,contrast)
    cv2.imshow('Effect', effect)

def apply_brightness_contrast(input_img, brightness = 255, contrast = 127):
    brightness = map(brightness, 0, 510, -255, 255)
    contrast = map(contrast, 0, 254, -127, 127)
    if brightness != 0:
        if brightness > 0:
            shadow = brightness
            highlight = 255
        else:
            shadow = 0
            highlight = 255 + brightness
        alpha_b = (highlight - shadow)/255
        gamma_b = shadow
        buf = cv2.addWeighted(input_img, alpha_b, input_img, 0, gamma_b)
    else:
        buf = input_img.copy()
    if contrast != 0:
        f = float(131 * (contrast + 127)) / (127 * (131 - contrast))
        alpha_c = f
        gamma_c = 127*(1-f)
        buf = cv2.addWeighted(buf, alpha_c, buf, 0, gamma_c)
    cv2.putText(buf,'B:{},C:{}'.format(brightness,contrast),(10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
    return buf

def map(x, in_min, in_max, out_min, out_max):
    return int((x-in_min) * (out_max-out_min) / (in_max-in_min) + out_min)

def alterImage():
    name = './pre-full.png'
    optimized_name = './optimized-full.png'
    img = cv2.imread(file_name+name)
    img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(gray, 0, 255,cv2.THRESH_BINARY_INV +cv2.THRESH_OTSU)
    kernel = np.ones((3, 3), np.uint8)
    closing = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE,kernel, iterations = 2)
    bg = cv2.dilate(closing, kernel, iterations = 1)
    dist_transform = cv2.distanceTransform(closing, cv2.DIST_L2, 0)
    ret, fg = cv2.threshold(dist_transform, 0.02*dist_transform.max(), 255, 0)
    cv2.imwrite(file_name+optimized_name, fg)
    cv2.imshow('image', fg)
    plt.figure(figsize=(10,10))

def compare():
    name = '/optimized-full.png'
    img = cv2.imread(file_name+name)
    img1 = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    box, label, count = cv.detect_common_objects(img, confidence=0.9)
    output = draw_bbox(img, box, label, count)
    print(f"count : {count}")
    output = cv2.cvtColor(output,cv2.COLOR_BGR2RGB)
    output = cv2.cvtColor(output,cv2.COLOR_BGR2RGB)
    plt.figure(figsize=(4,7))
    plt.axis('off')
    plt.imshow(output)
    plt.show()

def boxImage(name):
    img = cv2.imread(file_name+name)
    img1 = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    box, label, count = cv.detect_common_objects(img, confidence=0.9)
    output = draw_bbox(img, box, label, count)
    print(f"count : {count}")
    output = cv2.cvtColor(output,cv2.COLOR_BGR2RGB)
    output = cv2.cvtColor(output,cv2.COLOR_BGR2RGB)
    plt.figure(figsize=(4,7))
    plt.axis('off')
    plt.imshow(output)
    plt.show()
   

def snapInventory(name):
    pic = pyscreenshot.grab(bbox=(inventoryCoord[0], inventoryCoord[1], inventoryCoord[2], inventoryCoord[3]))
    pic.save(file_name + f"/{name}.png")
    img = cv2.imread(file_name+f"/{name}.png")
    effect = controller(img, 340, 212)
    cv2.imwrite(file_name+f'/result_{name}.png', effect)


def preAction(xRange, yRange):
    timeRange = [1,2]   #range to sleep
    #make an initial pic of inventory
    snapInventory('1')
    xBuffer = random.randint(xRange[0],xRange[1])
    yBuffer = random.randint(yRange[0],yRange[1])
    pyautogui.click(xBuffer,yBuffer)
    time.sleep(random.randint(timeRange[0],timeRange[1]))

def clickPosition(limit):
    countDown = limit
    xRange = [oreCoord[0], oreCoord[2]]
    yRange = [oreCoord[1], oreCoord[3]]
    timeRange = [6, 11]    #range to sleep
    while countDown >= 1:
        preAction(xRange, yRange)
        x = random.randint(xRange[0],xRange[1])
        y = random.randint(yRange[0],yRange[1])
        pyautogui.click(x,y)
        time.sleep(random.randint(timeRange[0],timeRange[1]))
        #make new pic of inventory
        snapInventory('2')
        winsound.PlaySound("SystemExit", winsound.SND_ALIAS)
        countDown = countDown - 1
        print(countDown)
        #compare past and present images and check if it is necessary to click again. 
        

done = False
 
def controller(img, brightness=255,
               contrast=127):
   
    brightness = int((brightness - 0) * (255 - (-255)) / (510 - 0) + (-255))
 
    contrast = int((contrast - 0) * (127 - (-127)) / (254 - 0) + (-127))
 
    if brightness != 0:
 
        if brightness > 0:
 
            shadow = brightness
 
            max = 255
 
        else:
 
            shadow = 0
            max = 255 + brightness
 
        al_pha = (max - shadow) / 255
        ga_mma = shadow
 
        # The function addWeighted calculates
        # the weighted sum of two arrays
        cal = cv2.addWeighted(img, al_pha,
                              img, 0, ga_mma)
 
    else:
        cal = img
 
    if contrast != 0:
        Alpha = float(131 * (contrast + 127)) / (127 * (131 - contrast))
        Gamma = 127 * (1 - Alpha)
 
        # The function addWeighted calculates
        # the weighted sum of two arrays
        cal = cv2.addWeighted(cal, Alpha,
                              cal, 0, Gamma)
 
    # putText renders the specified text string in the image.

 
    return cal



def displayDifferentImages():
    name='/pre-full.png'
    img = cv2.imread(file_name+name)
    img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(gray, 0, 255,cv2.THRESH_BINARY_INV +cv2.THRESH_OTSU)
    kernel = np.ones((3, 3), np.uint8)
    closing = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE,kernel, iterations = 2)
    bg = cv2.dilate(closing, kernel, iterations = 1)
    dist_transform = cv2.distanceTransform(closing, cv2.DIST_L2, 0)
    ret, fg = cv2.threshold(dist_transform, 0.02*dist_transform.max(), 255, 0)
    cv2.imshow('image', fg)
    plt.figure(figsize=(10,10))
    cv2.imwrite(file_name+'/gray.png', gray)
    cv2.imwrite(file_name+'/thresh.png', thresh)
    cv2.imwrite(file_name+'/closing.png', closing)
    cv2.imwrite(file_name+'/fg.png', fg)
    plt.subplot(2,2,1)
    plt.axis('off')
    plt.title("Original Image")
    plt.imshow(img,cmap="gray")
    
    plt.subplot(2,2,2)
    plt.imshow(gray,cmap="gray")
    plt.axis('off')
    plt.title("GrayScale Image")
    
    plt.subplot(2,2,3)
    plt.imshow(thresh,cmap="gray")
    plt.axis('off')
    plt.title("Threshold Image")
    
    plt.subplot(2,2,4)
    plt.imshow(fg,cmap="gray")
    plt.axis('off')
    plt.title("Segmented Image")
    
    plt.show()

    boxImage()
 #340 bightness, 212 constrast. 
if __name__ == '__main__':
    res = ''
    while(res != 'q'):
        print("s : Set Positons \n m : Mine Ore")
        print("What would you like to do? ")
        res = input("Action: ")
        if(res == 's'):
            print("Getting Ore coordinates.")
            getPosition("ore")
            print("Getting Inventory coordinates.")
            getPosition("inventory")
        if(res == 'm'):
            print("Starting to mine...")
            if(len(inventoryCoord) > 0):
                clickPosition(20)
            else:
                print("\nSet Positions first!")
                time.sleep(1)
            
    #clickOre()
    #displayDifferentImages()
    #alterImage()
    #compare()
    boxImage('/gray.png')
 
# The function waitKey waits for
# a key event infinitely  or for delay
# milliseconds, when it is positive.
done = True

    

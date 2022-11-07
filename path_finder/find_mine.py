#Goal: using a snap shot of the minimap located on the top-right of runeLite.
# locate the mining symbol. Then click said mining symbol to move towards it.

from sequential_tasks import seqClicker as sq
import pyscreenshot, cv2, os, time
import numpy as np
import matplotlib.pyplot as plt
import cvlib as cv
from cvlib.object_detection import draw_bbox
from PIL import Image


#Locate the map
#Locate the mine symbol
#grab coordinates of mine symbol in map
#click at said coordnates.


map_coord = []
mine_coord = []

def getMap():
    #getSnap of map
    #request a snapshot from seqClicker script.
    #retrieve the coordinates of the map.
    map_coord = sq.getPositions(1)
    print(f"MAP COORDINATE : {map_coord}")
    im = pyscreenshot.grab(bbox=(map_coord[0]))
    im.show()
    filename = "mine.jpg"
    cwd = os.getcwd()
    dirname = "{}/{}".format(cwd, "data/mine")
    if(os.path.exists(dirname) == False):
        os.mkdir(dirname)
    im = im.save("{}/{}".format(dirname, filename))

def setMineSymbol():
    map_coord = sq.getSquarePosition(110)
    print(f"MAP COORDINATE : {map_coord}")
    im = pyscreenshot.grab(bbox=(map_coord))
    im.show()
    filename = "map.png"
    cwd = os.getcwd()
    dirname = "{}/{}".format(cwd, "data/mine")
    if(os.path.exists(dirname) == False):
        os.mkdir(dirname)
    im = im.save("{}/{}".format(dirname, filename))

def examinePicture():
    name = ['mine-symbol.png', 'map.png']
    cwd = os.getcwd()
    symbolPath = "{}\data\mine\{}".format(cwd,name[0])
    mapPath  = "{}\data\mine\{}".format(cwd,name[1])
    print("Path : {}".format(symbolPath))
    print("Path : {}".format(mapPath))
    img = cv2.imread(symbolPath)
    #image = cv2.resize(img, (700,600))
    cv2.imshow("Image", img)
    cv2.waitKey(0)
    img = cv2.imread(mapPath)
    #image = cv2.resize(img, (700,600))
    cv2.imshow("Image", img)
    cv2.waitKey(0)
    symImg = Image.open(symbolPath)
    mapImg = Image.open(mapPath)
    symArray = np.asarray(symImg)
    mapArray = np.asarray(mapImg)
    print("Symbol : {} \n Map : {}".format(symArray, mapArray))
    if (symArray == mapArray).all(1).any():
        print("found")
    else: 
        print("not found")

    #cv2.imshow('image', fg)
    #plt.figure(figsize=(10,10))

def foundMine():
    #with the snap from getMap, locate the mine symbol
    #if mine symbol found, save coordinates by adding/subtracting to coords
    # of coordinate of map.
    # RETURN True IF FOUND  
    # else False

    return False



def clickMine():
    #only if foundMine == True
    #   get coordinates of mine, click at said coordinates.
    #Notify if clickMine is false
    pass

def prompt():
    examinePicture()
    print("Looking for mine")
    if(foundMine()):
        print("Found a mine")
    else:
        print("No mine found")

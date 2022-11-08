#Goal: using a snap shot of the minimap located on the top-right of runeLite.
# locate the mining symbol. Then click said mining symbol to move towards it.

from sequential_tasks import seqClicker as sq
import pyscreenshot, cv2, os, time, sys
import numpy as np
import matplotlib.pyplot as plt
import cvlib as cv
from cvlib.object_detection import draw_bbox
from PIL import Image
import pandas as pd
np.set_printoptions(threshold=sys.maxsize)


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
    name = ['mine-symbol.png', 'map.png', 'map1.png']
    cwd = os.getcwd()
    symbolPath = "{}\data\mine\{}".format(cwd,name[0])
    mapPath  = "{}\data\mine\{}".format(cwd,name[1])
    map1Path  = "{}\data\mine\{}".format(cwd,name[2])
    img = cv2.imread(symbolPath)
    #image = cv2.resize(img, (700,600))
    #cv2.imshow("Image", img)
    #cv2.waitKey(0)
    img = cv2.imread(mapPath)
    #image = cv2.resize(img, (700,600))
    #cv2.imshow("Image", img)
    #cv2.waitKey(0)
    
    symImg = Image.open(symbolPath)
    mapImg = Image.open(mapPath)
    map1Img = Image.open(map1Path)
    symArray = np.asarray(symImg)
    mapArray = np.asarray(mapImg)
    map1Array = np.asarray(map1Img)
    print("Symbol : {} \n Map : {}".format(symArray[0][0], symArray[0][0]))
    print(np.array_equal(mapArray, map1Array))
    print(np.where(pd.Index(pd.unique(symArray[11][0])).get_indexer(mapArray[0][0]) >= 0)[0])

    newSet = []
    for i in range(mapArray.shape[0]):
        #default counter start points
        mapIndex = i
        symIndex = 0
        found = 0
        newSet = []
        while(i < (mapArray.shape[0] - symArray.shape[0])):
            if (symIndex >= symArray.shape[0]):
                symIndex = 0
                mapIndex += 1
            unkonwnSetSize = np.where(pd.Index(pd.unique(symArray[symIndex][0])).get_indexer(mapArray[mapIndex][mapIndex+symIndex]) >= 0)[0].shape[0]
            defaultSetSize = symArray.shape[2]
            if(unkonwnSetSize == defaultSetSize):
                found += 1
                newSet.append(mapArray[mapIndex][mapIndex+symIndex])
            if(unkonwnSetSize != defaultSetSize):
                break
            if(found == symArray.shape[0]):
                print("found!!!!!")
                break
        if(found == symArray.shape[0]):
            break

    print(newSet)
    print(symArray)
                
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

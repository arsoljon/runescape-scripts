#Goal: using a snap shot of the minimap located on the top-right of runeLite.
# locate the mining symbol. Then click said mining symbol to move towards it.

from sequential_tasks import seqClicker as sq
import pyscreenshot, cv2, os, time
import numpy as np
import matplotlib.pyplot as plt
import cvlib as cv
from cvlib.object_detection import draw_bbox


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
    filename = "inv-zoomed-out.png"
    cwd = os.getcwd()
    dirname = "{}/{}".format(cwd, "data/mine")
    if(os.path.exists(dirname) == False):
        os.mkdir(dirname)
    im = im.save("{}/{}".format(dirname, filename))

def examinePicture():
    name = ['mine-symbol.png', 'inv-half-zoomed-in.png', 'inv-zoomed-out.png']
    cwd = os.getcwd()
    path = "{}\data\mine\{}".format(cwd,name[0])
    test_path = "{}/data/mine/testing.png".format(cwd)
    print("Path : {}".format(path))
    img = cv2.imread(path)
    image = cv2.resize(img, (700,600))
    cv2.imshow("Image", image)
    cv2.waitKey(0)
    filename = "enlarged-pickaxe.png"
    cwd = os.getcwd()
    dirname = "{}/{}".format(cwd, "data/mine")
    if(os.path.exists(dirname) == False):
        os.mkdir(dirname)
    cv2.imwrite("{}/data/mine/{}".format(cwd, filename), image)
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
    #setMineSymbol()
    getMap()
    if(foundMine()):
        print("Found a mine")
    else:
        print("No mine found")

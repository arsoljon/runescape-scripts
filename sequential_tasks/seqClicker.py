#Goal: Subsequently click different objectives. 

#   Change the values, timeRange & timebetweencoords, for quicker clicking and setup

import random, pyautogui, time, winsound
#from numpy import append
import win32api, win32con
from pywinauto import Application
import pywinauto as pwa
import json
#import win32gui
#from overlay import Window

timeRange = [999,999]
timebetweencoords = 4
config_file_path = "./data/config.json"

def setup():
    global timeRange, timebetweencoords
    with open(config_file_path, 'r', encoding="utf-8") as f:
        config = json.loads(f.read())
    timeRange = [config["timeBetweenClicks"]["low"], config["timeBetweenClicks"]["high"]]
    timebetweencoords = config["timeBetweenCoords"]
    
def editPrompt():
    printCurrentConfig()
    lowTR = int(input("Minimum seconds between clicks: "))
    highTR = int(input("Maximum seconds between clicks: "))
    tbc = int(input("Saving Coordinate buffer: "))
    editConfig(lowTR, highTR, tbc)
    setup()

def editConfig(lowTR, highTR, tbc):   
    with open(config_file_path, 'r', encoding="utf-8") as f:
        config = json.loads(f.read())
    config["timeBetweenClicks"]["low"] = lowTR
    config["timeBetweenClicks"]["high"] = highTR
    config["timeBetweenCoords"] = tbc
    with open(config_file_path, 'w') as f:
        json.dump(config, f)

def printCurrentConfig():
    print(f"Time between clicks : {timeRange[0]}s - {timeRange[1]}s\nSaving Coordinate buffer : {timebetweencoords}s\n")

def preClick(xRange, yRange):
    #preclick is used to make sure window is in the forefront. 
    #also helps increase randomness of clicks to avoid bot detection. 
    xBuffer = random.randint(xRange[0],xRange[1])
    yBuffer = random.randint(yRange[0],yRange[1])
    pyautogui.click(xBuffer,yBuffer)
    time.sleep(random.randint(1,2))

def clickPositions(cycles, locations):
    #Click through the sequence of locations.
    for i in range(cycles):
        for j in range(len(locations)):
            xRange = [locations[j][0], locations[j][2]]
            yRange = [locations[j][1], locations[j][3]]
           
            preClick(xRange, yRange)
            x = random.randint(xRange[0],xRange[1])
            y = random.randint(yRange[0],yRange[1])
            pyautogui.click(x,y)
            #hideLeftClick(x,y)
            #hideLeftClick(x,y)
            time.sleep(random.randint(timeRange[0],timeRange[1]))
    #Done with all iterations.
    winsound.PlaySound("SystemExit", winsound.SND_ALIAS)
    print("CYCLES DONE")

def getSquarePosition(length):
    print("Place cursor in center of wanted area.")
    coordinate = []
    radius = int(length / 2)
    buffer = timebetweencoords 
    time.sleep(2)
    while buffer >= 1: 
        print(f"{buffer}...")
        buffer -= 1
        time.sleep(1)
    coordinate = pyautogui.position()
    x1 = coordinate[0] - radius
    y1 = coordinate[1] - radius
    x2 = coordinate[0] + radius
    y2 = coordinate[1] + radius
    return ([x1,y1,x2,y2])

def getPositions(obj_count):
    allCoords = []
    print("\nHover over 1 corner of each objective until countdown is finished.")
    print("Then move to next corner of objective.\n")
    time.sleep(2)
    for i in range(obj_count):
        print(f"Getting coordinates for new Objective {i + 1}: ")
        index = 0
        coordinateSet = []
        while index < 4:
            buffer = timebetweencoords 
            while buffer >= 1: 
                print(f"{buffer}...")
                buffer -= 1
                time.sleep(1)
            print(f"Coordinate {index + 1}/4 received")
            currentLocation = pyautogui.position()
            #append location to list of coordinates. 
            coordinateSet.append(currentLocation)
            index += 1
            if(index >= 4):
                print(f"Objective {i+1} DONE")
        #take lowest and highest x1, y1, x2, y2 values and put them in a list; 
        # [x1Min, y1Min, x2Max, y2Max] 
        x1 = min(coordinateSet[0][0], coordinateSet[1][0], coordinateSet[2][0], coordinateSet[3][0])
        y1 = min(coordinateSet[0][1], coordinateSet[1][1], coordinateSet[2][1], coordinateSet[3][1])
        x2 = max(coordinateSet[0][0], coordinateSet[1][0], coordinateSet[2][0], coordinateSet[3][0])
        y2 = max(coordinateSet[0][1], coordinateSet[1][1], coordinateSet[2][1], coordinateSet[3][1])
        someList = [x1, y1, x2, y2]
        #save the coordinates for the first objective
        allCoords.append(someList)
    print(f"Recieved Cordinates for {obj_count} objective(s).")
    return allCoords



def hideLeftClick(x,y):
    #mouse_event coordinates work differently than previously assumed. 
    #refer to video to adjust using the method used. 
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
    time.sleep(.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)
    print('Left Click')

def practice():
    app = Application().connect(process=13100)
    time.sleep(2)
    dlg = app.RuneLite
    dialogs = app.windows()
    temp = app.window(title_re=".*jinzo no.*")
    pid = pwa.handleprops.processid(dialogs[0])
    rect = pwa.handleprops.rectangle(dialogs[0])    #(L4, T5, R869, B1011)


def prompt():
    setup()
    printCurrentConfig()
    print("The sequence of clicks is decided while getting the\ncoordinates of each objective.\n")
    response = input("Edit settings (y/n)? ")
    if response == 'y':
        editPrompt()
    obj_count = int(input("How many objectives? "))
    locations = getPositions(obj_count)
    cycles = int(input("How many cycles? "))
    #print(locations)
    clickPositions(cycles, locations)
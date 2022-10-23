#Goal: Subsequently click different locations. 
#Instructions: 
#   run getPostions() to get general cos for different objectives
#ordinate


import random, pyautogui, time, winsound
from numpy import append
import win32api, win32con, win32gui
from pywinauto import Application
import pywinauto as pwa

inventoryCoord = []
oreCoord = []

def preAction(xRange, yRange):
    timeRange = [1,2]   #range to sleep
    xBuffer = random.randint(xRange[0],xRange[1])
    yBuffer = random.randint(yRange[0],yRange[1])
    pyautogui.click(xBuffer,yBuffer)
    time.sleep(random.randint(timeRange[0],timeRange[1]))

def clickPositions(cycles, locations):
    for i in range(cycles):
        for j in range(len(locations)):
            xRange = [locations[j][0], locations[j][2]]
            yRange = [locations[j][1], locations[j][3]]
            timeRange = [1, 2]    #range to sleep
            #preAction(xRange, yRange)
            x = random.randint(xRange[0],xRange[1])
            y = random.randint(yRange[0],yRange[1])
            #pyautogui.click(x,y)
            hideLeftClick(x,y)
            hideLeftClick(x,y)
            time.sleep(random.randint(timeRange[0],timeRange[1]))
        winsound.PlaySound("SystemExit", winsound.SND_ALIAS)

def getPositions(obj_count):
    allCoords = []
    print("Get the four corners representing your objective.")
    for i in range(obj_count):
        print(f"Getting coordinates for Objective {i + 1}: ")
        index = 0
        coordinateSet = []
        while index < 4:
            buffer = 5 
            while buffer >= 1: 
                print(f"{buffer}...")
                buffer -= 1
                time.sleep(1)
            print(f"Coordinate {index + 1}/4 received")
            currentLocation = pyautogui.position()
            #append location to list of coordinates. 
            coordinateSet.append(currentLocation)
            index += 1
        #take lowest and highest x1, y1, x2, y2 values and put them in a list; 
        # [x1Min, y1Min, x2Max, y2Max] 
        x1 = min(coordinateSet[0][0], coordinateSet[1][0], coordinateSet[2][0], coordinateSet[3][0])
        y1 = min(coordinateSet[0][1], coordinateSet[1][1], coordinateSet[2][1], coordinateSet[3][1])
        x2 = max(coordinateSet[0][0], coordinateSet[1][0], coordinateSet[2][0], coordinateSet[3][0])
        y2 = max(coordinateSet[0][1], coordinateSet[1][1], coordinateSet[2][1], coordinateSet[3][1])
        someList = [x1, y1, x2, y2]
        #save the coordinates for the first objective
        allCoords.append(someList)
    print(f"Recieved Cordinates for {obj_count} objectives.")
    return allCoords

def hideLeftClick(x,y):
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
    time.sleep(.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)
    print('Left Click')



if __name__ == "__main__":
    app = Application().connect(process=13100)
    time.sleep(2)
    dlg = app.RuneLite
    dialogs = app.windows()
    temp = app.window(title_re=".*jinzo no.*")
    pid = pwa.handleprops.processid(dialogs[0])
    rect = pwa.handleprops.rectangle(dialogs[0])    #(L4, T5, R869, B1011)

    obj_count = int(input("How many objectives? "))
    locations = getPositions(obj_count)
    cycles = int(input("How many cycles? "))
    print(locations)
    clickPositions(cycles, locations)
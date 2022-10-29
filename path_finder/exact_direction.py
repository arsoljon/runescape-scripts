import random, pyautogui, time, winsound
import win32api, win32con
from pywinauto import Application
import pywinauto as pwa
from sequential_tasks import seqClicker as sc

#get coordinate and objectives using getposition and click positions

clicks = 8
maxTime = 33
furnace = []
mining = []

def setFurnaceDir():
    global furnace
    print("Get coordinates for the direction of the furnace in the minimap.")
    furnace = sc.getPositions(1)

def setMiningDir():
    global mining
    print("Get coordinates for the direction of the mining area in the minimap.")
    mining = sc.getPositions(1)
    
def gotoFurnace():
    sc.clickPositions(8, furnace)

def gotoMining():
    sc.clickPositions(8, mining)

def startProcess(location):
    setFurnaceDir()
    setMiningDir()
    if location == "furnace":
        gotoFurnace()
    if location == "mining":
        gotoMining()
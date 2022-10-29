#Goal: using a snap shot of the minimap located on the top-right of runeLite.
# locate the mining symbol. Then click said mining symbol to move towards it.

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
    pass

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
    print("Looking for mine")
    getMap()
    if(foundMine()):
        print("Found a mine")
    else:
        print("No mine found")

'''
Day 3: Perfectly Spherical Houses in a Vacuum

input is line of text containing direction characters (<>^v)
Part 1: follow path; how many unique locations are visited 
(e.g. count each location no more than once)
Answer is 2592

Part 2 same but there are two santa's who alternate moves.  
Answer is 2360

'''

inputFile = 'data/Day 3 InputTEMP.txt'
inputFile = 'data/Day 3 Input.txt'


directionStr = str()

def parseInput():
    global directionStr

    # input is one line of direction characters
    directionStr = (open(inputFile, 'r')).readline()


def getNextLoc(dirChar:str, x:int, y:int):
    
    if dirChar == 'v':
        y -= 1
    elif dirChar == '^':
        y += 1
    elif dirChar == '>':
        x += 1
    elif dirChar == '<':
        x -= 1
    else:
        print (f'BAD dirChar {dirChar=}')
        exit()
    return (x,y)
    

def doIt():
    global directionStr

    # part 1
    locationSetPt1 = { (0,0) }
    xCoord:int = 0; yCoord:int = 0
    for dirChar in directionStr:
        (xCoord,yCoord) = getNextLoc(dirChar, xCoord, yCoord)
        locationSetPt1.add( (xCoord,yCoord) )

    # part 2
    locationSetPt2 = { (0,0) }
    xCoordSanta:int = 0; yCoordSanta:int = 0
    xCoordRobot:int = 0; yCoordRobot:int = 0
    isSantasTurn = True
    for dirChar in directionStr:

        if isSantasTurn:
            (xCoordSanta,yCoordSanta) = getNextLoc(dirChar, xCoordSanta, yCoordSanta)
            locationSetPt2.add( (xCoordSanta,yCoordSanta) )
        else:
            (xCoordRobot,yCoordRobot) = getNextLoc(dirChar, xCoordRobot, yCoordRobot)
            locationSetPt2.add( (xCoordRobot,yCoordRobot) )
        isSantasTurn = not isSantasTurn

    print(f'Part 1: {len(locationSetPt1)}')
    print(f'Part 2: {len(locationSetPt2)}')


def main():
    parseInput()
    doIt()
    return

main()

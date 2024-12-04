'''
day 6 part2 count total brightness of all lights with new rules
lights at each corner are at 0,0, 0,999, 999,999, and 999,0

turn on 0,0 through 999,999 would increase the brightness of those lights by 1
toggle increase the brightness of those lights by 2.
turn off - decrease the brightness of those lights by 1, to a minimum of zero.

Each coordinate pair represents opposite corners of a rectangle, inclusive;
  a coordinate pair like 0,0 through 2,2 therefore refers to
  9 lights in a 3x3 square. The lights all start turned off.

  Answer is 14110788
 
'''
inputFile = 'Day 6 Input.txt'

GRID_SIZE = 999
gridList = [] # will be GRID_SIZE list of GRID_SIZE strings

ON = 0; OFF = 1; TOGGLE = 2; INVALID = -1 # Command opcodes

litCount = 0

def printGrid():
    global gridList
    if GRID_SIZE < 80:
        for i in range(0,GRID_SIZE+1):
             print(gridList[i])
        print(' ')

def initGrid():
    global gridList



    gridList = [[0] for i in range(GRID_SIZE+1)]
    for i in range (0,GRID_SIZE+1):
        for j in range(1,GRID_SIZE+1):
            gridList[i].append(0)

    

    printGrid()

def extractCoordinates(coordinateStr):
    start,thru,end = coordinateStr.split(' ')
    startRow, startCol = start.split(',')
    endRow, endCol = end.split(',')
    return int(startRow),int(startCol),int(endRow),int(endCol)

def processToggle(startRow,startCol,endRow,endCol):
    global gridList
    for i in range(startRow,endRow+1):
        for j in range(startCol,endCol+1):
            gridList[i][j] += 2
                

    return

def processOn(startRow,startCol,endRow,endCol):
    global gridList
    for i in range(startRow,endRow+1):
        for j in range(startCol,endCol+1):
            gridList[i][j] += 1
        
    return

def processOff(startRow,startCol,endRow,endCol):
    global gridList
    for i in range(startRow,endRow+1):
        for j in range(startCol,endCol+1):
            gridList[i][j] -= 1
            gridList[i][j] = max(gridList[i][j],0)
       
    return



def doIt():
    global gridList, litCount 
    opcode = INVALID
    startScan = 0
    for line in open(inputFile,'r'):
        line = line.rstrip()
        if line[0:7] == 'turn on':
            opCode = ON
            startScan = 8
        elif line[0:8] == 'turn off':
            opCode = OFF
            startScan = 9
        elif line[0:6] == 'toggle':
            opCode = TOGGLE
            startScan = 7
        else:
            print(f'ERROR {line=}')
        startRow,startCol,endRow,endCol = extractCoordinates(line[startScan:])
#        print(f'{line=} {opCode=} ')
#        print(f'{startRow=} {startCol=}    {endRow=} {endCol=}')

        if opCode == TOGGLE:
            processToggle(startRow,startCol,endRow,endCol)
        elif opCode == ON:
            processOn(startRow,startCol,endRow,endCol)
        else:
            processOff(startRow,startCol,endRow,endCol)

            
        
        printGrid()                
                 

    for i in range(len(gridList)):
        for j in range(len(gridList)):
            litCount += gridList[i][j]

            
    print(f'pt2 count is {litCount}')
            

def main():
    initGrid()
    doIt()
    return

main()

'''
day 6 count lit lights -- part 1
lights at each corner are at 0,0, 0,999, 999,999, and 999,0

turn on 0,0 through 999,999 would turn on every light
toggle
turn off

Each coordinate pair represents opposite corners of a rectangle, inclusive;
  a coordinate pair like 0,0 through 2,2 therefore refers to
  9 lights in a 3x3 square. The lights all start turned off.

  Answer is 377891

NOTES:
Alomost all solvers used list of lists.  I used lists of strings for performance reasons.


 
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

def initGrid():
    global gridList
    for i in range(0,GRID_SIZE+1):
        gridList.append('.'*GRID_SIZE)
    printGrid()

def extractCoordinates(coordinateStr):
    start,thru,end = coordinateStr.split(' ')
    startRow, startCol = start.split(',')
    endRow, endCol = end.split(',')
    return int(startRow),int(startCol),int(endRow),int(endCol)

def processToggle(startRow,startCol,endRow,endCol):
    for i in range(startRow, endRow+1):
        front = gridList[i][0:startCol]
        end = gridList[i][endCol+1:]
        middleList = list(gridList[i][startCol:endCol+1])
        for k in range(0,len(middleList)):
            if middleList[k] == '.':
                middleList[k] = '*'
            else:
                middleList[k] = '.'
            middleString = "" 
     
        for ele in middleList: 
            middleString += ele 
            gridList[i] = front + middleString + end
                

    return

def processOnOff(opCode, startRow,startCol,endRow,endCol):
    global gridList
    if opCode == ON:
        char = '*'
    else:
        char = '.'
    middleString = char* (endCol+1-startCol)
    for i in range(startRow, endRow+1):
        gridList[i] = gridList[i][0:startCol] + \
                      middleString \
                      + gridList[i][endCol+1:]         
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
        else:
            processOnOff(opCode, startRow,startCol,endRow,endCol)
        
        printGrid()                
                 

    for i in range(len(gridList)):
        litCount += gridList[i].count('*')
        
        
    print(f'pt1 count is {litCount}')
            

def main():
    initGrid()
    doIt()
    return

main()

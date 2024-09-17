'''
Day 1: Not Quite Lisp

input is string of '(' and ')' 
Part 1: sum string where '(' = +1 and')' = -1 Answer is 232

Part 2 what character position first puts us into the basement.  Answer is 1783 

'''

inputFile = 'Day 1 InputTEMP.txt' 
inputFile = 'Day 1 Input.txt'

line = ''


def parseInput():
    global line

    line = open(inputFile, 'r').readline()
    

def doIt():

    # part 1 & ppart 2
    currentFloor:int = 0
    charsToBasement:int = 0;  p2:int = 0 # part 2 
    for c in line:
        if c == '(':
            currentFloor += 1
        elif c == ')':
            currentFloor -=1
        charsToBasement += 1
    
        if currentFloor == -1 and p2 == 0:
            p2 = charsToBasement

    print(f'Part 1: {currentFloor}')
    print(f'Part 2: {p2}')


def main():
    parseInput()
    doIt()
    return

main()

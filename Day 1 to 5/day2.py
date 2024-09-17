'''
Day 2: I Was Told There Would Be No Math

input is lines of the form: 3x11x24  aka l w h
Part 1: 2*(l*w + w*h + h*l) + min(l*w, w*h, h*l)
Answer is 1588178 

Part 2 A present with dimensions 2x3x4 requires 2+2+3+3 = 10 feet of ribbon to wrap the present 
plus 2*3*4 = 24 feet of ribbon for the bow, for a total of 34 feet.
That is: smallest perimeter plus l*w*h
Answer is 3783758 

'''
inputFile = 'Data/Day 2 InputTEMP.txt'
inputFile = 'Data/Day 2 Input.txt'


packageList = list()

def parseInput():
    global packageList
    # find 3 numbers seperated by x's - convert to ints and store as a tuple
    for line in open(inputFile, 'r') :
        lineList = [int(i) for i in line.strip('\n').split('x')]
        packageList.append(tuple(lineList) )

def calcWrappingPaper(l: int, w:int, h: int)-> int:
    return  2*(l*w + w*h + h*l) + min(l*w, w*h, h*l)

def calcRibbon(l: int, w:int, h: int)-> int:
    # find two smallest numbers
    num1 = min(l,w)
    num2 = min(max(l,w),h)
    # calc perimeter and volume
    perimeter:int = 2*(num1+num2)
    volume:int = l*w*h
    return perimeter + volume

def doIt():

    pt1 = 0; pt2 = 0

    for item in packageList:
        l,w,h = item
        pt1 += calcWrappingPaper(l,w,h)
        pt2 += calcRibbon(l,w,h)

    print(f'Part 1: {pt1}')
    print(f'Part 2: {pt2}')


def main():
    parseInput()
    doIt()
    return

main()

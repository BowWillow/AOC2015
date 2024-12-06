'''
day 7: Some Assembly Required
input are circuit elements (see problem statement)
 part 1 run the circuit; what signal is ultimately provided to wire a
 answer is 3176

 For part 2 change the input file (to 'Day 7 Input2'):
  line that read 44430 -> b is   changed to 3176 ->b; run it
  answer is 14710

  Note: our strategy is to build a table of all instructions
  on each pass we execute the ones that we are able and repeat 
  until there are none left

'''

inputFile = '../Data/Day 7 Input.txt'
inputFile = '../Data/Day 7 Input2.txt'

instList = []
resolvedDict = dict()


# convertNumber adds a literal to the resolve dictionary
def convertNumber(word):
    global resolvedDict
    resolvedDict['L'+word] = int(word)
    return 'L'+word


# processTwoOperand handles commands with two operands
def processTwoOperand(line):
    global resolvedDict, instList
    wordList = line.split(' ')
    cmd = wordList[1]
    outWire = wordList[4]
    if wordList[0].isdigit():
        wordList[0] = convertNumber(wordList[0])
    if wordList[2].isdigit():
        wordList[0] = convertNumber(wordList[2])
    opList = [wordList[0], wordList[2]]

    return opList, cmd, outWire, 0


# processOneOperand processes commands with one operand
def processOneOperand(line):
   
    wordList = line.split(' ')
    if wordList[0] == 'NOT':
        opList = [wordList[1]]
        outWire = wordList[3]
        cmd = wordList[0]
        modifier = 0
    else:
        opList = [wordList[0]]
        cmd = wordList[1]
        modifier = int(wordList[2])
        outWire = wordList[4]
    return opList, cmd, outWire, modifier


# processZeroOperand process commands with no operands
def processZeroOperand(line):
    global resolvedDict, instList
    wordList = line.split(' ')
    if wordList[0].isdigit():
        resolvedDict[wordList[2]] = int(wordList[0])
    else:
        opList = [wordList[0]]
        cmd = 'EQ'
        outWire = wordList[2]  
        instList.append( (opList, cmd, outWire, 0) )      
    return


def parseInput():
    for line in open(inputFile,'r'):
        line = line.strip()
        if line.find('OR') >= 0 or line.find('AND') >= 0:
            instList.append( (processTwoOperand(line)) )
        elif line.find('NOT') >= 0 or line.find('SHIFT') >= 0 :
            instList.append( (processOneOperand(line)) )
        else:
            processZeroOperand(line)


# doCmd executes one instruction
def doCmd (opList, cmd, outWire, modifier):
    global resolvedDict
    if cmd == 'NOT':
        tmp = ~resolvedDict[opList[0]] 
        if tmp < 0:
            tmp = 65536 + tmp
        resolvedDict[outWire] = tmp
    elif cmd == 'AND':
        resolvedDict[outWire] = resolvedDict[opList[0]] & resolvedDict[opList[1]]
    elif cmd == "OR":
        resolvedDict[outWire] = resolvedDict[opList[0]] | resolvedDict[opList[1]]
    elif cmd == 'LSHIFT':
        resolvedDict[outWire] = resolvedDict[opList[0]] << modifier
    elif cmd == 'RSHIFT':
        resolvedDict[outWire] = resolvedDict[opList[0]] >> modifier
    elif cmd == 'EQ':
        resolvedDict[outWire] = resolvedDict[opList[0]]
    else:
        print(f'ERROR Invalid Command')


def doIt():
    global instList, resolvedDict

    doneFlag = False
    removeList = []

    while not doneFlag:
        # find commands that we can execute
        for opList, cmd, outWire, modifier in instList:
            opsLive = True
            for ops in opList: 
                if not ops in resolvedDict:
                    opsLive = False
        # execute them
            if opsLive:
                doCmd(opList, cmd, outWire, modifier)
                removeList.append( (opList, cmd, outWire, modifier) )
        if len(removeList) == 0:
            doneFlag = True
            print(f'ERROR some wires are unresolved')
        # remove them from the instruction list
        for item in removeList:
            instList.remove( item )
            removeList = []
        if instList == []:
            doneFlag = True
    
    print(f"Part 1 or 2 {resolvedDict['a']}")
            

def main():
    parseInput()
    doIt()
    return

main()

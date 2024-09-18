'''
Day 5: Doesn't He Have Intern-Elves For This?

input is one string per line such as sszojmmrrkwuftyv
Part 1: count of 'nice' strings were nice is:
  It contains at least three vowels (aeiou only), like aei.
  It contains at least one letter that appears twice in a row, like abcdde (dd).
  It does not contain the strings ab, cd, pq, or xy, 
     even if they are part of one of the other requirements.
Answer is 255 

Part 2 count of 'nice' strings where nice is:  
  It contains a pair of any two letters that appears at least twice in the string 
    without overlapping, like xyxy (xy) or aabcdefgaa (aa), but not like aaa (aa, but it overlaps).
  It contains at least one letter which repeats with exactly one letter between them, 
    like xyx, or even aaa.
Answer is 55 

'''
inputFile = 'Data/Day 5 InputTEMP.txt'
inputFile = 'Data/Day 5 Input.txt'

inputList = list()  # a list of strings stored as '*string***'
                    # the stars are so we can compare without special casing the start and end of string

def parseInput():
    global tempList

    for line in open(inputFile, 'r') :
        inputList.append('*' + line.strip('\n') + '***')

def lookForDuplicatePair(pairSet, searchStr):

    # if four characters in a row are equal (e.g.'bbbb'), we are done
    if searchStr[0] == searchStr[1] and searchStr[1] == searchStr[2] and searchStr[2] == searchStr[3] :
        return True
    # if 3 characters in a row are equal, skip
    if searchStr[0] == searchStr[1] and searchStr[1] == searchStr[2]:
        return False
    # if first 2 characters already in pairSet, we are done
    if searchStr[0:2] in pairSet:
        return True
    else:
        # add first 2 characters to pairSet
        pairSet.add(searchStr[0:2])
    return False

def doIt():
    global inputList

    niceCountPt1 = 0; niceCountPt2 = 0
    for candidate in inputList:
        
        vowelCount = 0; twiceInARowFound = False; forbiddenString = False
        pairSet = set(); matchingPairFound = False; repeatingLetter = False
        for i in range(1,len(candidate)-3):
            # part 1
            # at least 3 vowels
            if candidate[i] in {'a', 'e', 'i', 'o', 'u'}:
                vowelCount += 1
            # one letter that appears twice in a row
            if candidate[i] == candidate[i-1]:
                twiceInARowFound = True
            # does not contain  ab, cd, pq, or xy
            # print(f'{candidate[i-1:i+1]}')
            if candidate[i-1:i+1] in {'ab', 'cd', 'pq', 'xy'}:
                forbiddenString = True

            # part 2
        #   It contains a pair of any two letters that appears at least twice in the string 
        #     without overlapping, like xyxy (xy) or aabcdefgaa (aa), but not like aaa (aa, but it overlaps).
            if lookForDuplicatePair(pairSet, candidate[i:i+4]):
                matchingPairFound = True

        #   It contains at least one letter which repeats with exactly one letter between them, 
        #     like xyx, or even aaa.
            if candidate[i] == candidate[i+2]:
                repeatingLetter = True




        # is part1 nice?
        if vowelCount >=3 and twiceInARowFound and not forbiddenString:
            niceCountPt1 += 1

        # is part 2 nice?
        if matchingPairFound and repeatingLetter:
            niceCountPt2 += 1


    print(f'Part 1: {niceCountPt1=}')
    print(f'Part 2: {niceCountPt2=}')


def main():
    parseInput()
    doIt()
    return

main()

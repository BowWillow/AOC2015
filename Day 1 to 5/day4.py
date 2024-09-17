'''
Day 4: The Ideal Stocking Stuffer

input is yzbqklnj
Part 1: take input concatenated with a number.
Answer is lowest number with resulting (hex) hash containing 5 leading zeros
Answer is 282749


Part 2 same but 6 leading zeroes  
Answer is 9962624

'''

import hashlib









def main():

    keyPrefix = 'yzbqklnj'  # puzzle input
    pt1Found = False; fiveZeroes = '00000'
    pt2Found = False; sixZeroes = '000000'
    keySuffix = 0

    while not pt2Found:
        # parm1: the full key
        # encode creates the (binary) hash
        # hexdigest converts to hex
        h = hashlib.md5((keyPrefix + str(keySuffix)).encode()).hexdigest()

        if not pt1Found and h[:5] == fiveZeroes:
            print(f'Part 1: {keySuffix=}  {h=}')
            pt1Found = True 

        if h[:6] == '000000':
            print(f'Part 2: {keySuffix=}  {h=}')
            pt2Found = True 

        keySuffix += 1  

    return

main()

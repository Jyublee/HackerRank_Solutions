#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'chocolateInBox' function below.
#                                                        421            421
# The function is expected to return an INTEGER.         011            101         5
# The function accepts INTEGER_ARRAY arr as parameter.   010            011         3
#

def chocolateInBox(arr):
    xo = 0
    for x in arr:
        xo ^= x
    if xo == 0: 
        return 0
    c = 0
    for x in arr:
        if x ^ xo < x: 
            c += 1
    return c
        
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = chocolateInBox(arr)

    fptr.write(str(result) + '\n')

    fptr.close()

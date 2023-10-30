#!/bin/python3

import math
import os
import random
import re
import sys
import operations
#
# Complete the 'chocolateInBox' function below.
#                                                        421            421
# The function is expected to return an INTEGER.         011            101         5
# The function accepts INTEGER_ARRAY arr as parameter.   010            011         3
#

def chocolateInBox(arr):
    r=0
    for i in arr:
        r^=i 
    if(r==0):
        return(0)
    else:
        return(r)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = chocolateInBox(arr)

    fptr.write(str(result) + '\n')

    fptr.close()

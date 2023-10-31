#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'isValid' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def isValid(s):
    set_list = list(s)
    freq = {}
    for item in set_list:
        if item in freq:
            freq[item] += 1
        else:
            freq[item] = 1
    freq_of_freq = list(freq.values())
    freq_of_freq_counts = set(freq_of_freq)
    
    if len(freq_of_freq_counts) == 1:
        return "YES"
    else:
        freq_freq = {}
        for item in freq_of_freq:
            if item in freq_freq:
                freq_freq[item] += 1
            else:
                freq_freq[item] = 1
        theValues = list(freq_freq.values())
        theKeys = list(freq_freq.keys())
        if len(theValues) == 2:
            if theKeys[1] - theKeys[0] <= 1 and theValues[1] == 1:
                return "YES"
            else:
                return "NO"
        else:
            return "NO"

# You can call this function with your input string 's' to get the result.


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()

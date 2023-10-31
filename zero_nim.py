#!/bin/python3

import sys


g = int(input().strip())
for a0 in range(g):
    n = int(input().strip())
    p = [int(p_temp) for p_temp in input().strip().split(' ')]
    # your code goes here
    result = 0
    for a in p:
        if(a%2==0):
            a = a-1
        else:
            a = a+1
        result ^= a
    if result == 0:
        print("L")
    else:
        print("W")

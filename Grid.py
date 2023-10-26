#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gridSearch' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING_ARRAY G
#  2. STRING_ARRAY P

def gridSearch(G, P):
    H, W = len(G), len(G[0])
    h, w = len(P), len(P[0])
     
    for i in range(H):
        start_idx = G[i].find(P[0])
         
        if start_idx != -1:
            while start_idx != -1:

                j = 1
                while j < h and G[i+j][start_idx:start_idx+w] == P[j]:
                    j += 1
                     
                if j == h:
                    return "YES"
                 
                start_idx = G[i].find(P[0], start_idx+1) 
    return "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        R = int(first_multiple_input[0])

        C = int(first_multiple_input[1])

        G = []

        for _ in range(R):
            G_item = input()
            G.append(G_item)

        second_multiple_input = input().rstrip().split()

        r = int(second_multiple_input[0])

        c = int(second_multiple_input[1])

        P = []

        for _ in range(r):
            P_item = input()
            P.append(P_item)

        result = gridSearch(G, P)

        fptr.write(result + '\n')

    fptr.close()

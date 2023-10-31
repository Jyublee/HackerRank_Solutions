#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'arrayManipulation' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#

N, M = map(int, input().split())
A = [0 for i in range(N+2)]
for i in range(M):
    a, b, k = map(int, input().split())
    A[a] += k
    A[b + 1] -= k
for i in range(1, len(A)):
    A[i] += A[i-1]
print(max(A))

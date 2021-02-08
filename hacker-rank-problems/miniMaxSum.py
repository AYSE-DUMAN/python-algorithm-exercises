#!/bin/python3

import math
import os
import random
import re
import sys



# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    s = sorted(arr)
    s_min = sum(s[0:-1])
    s_max = sum(s[1:])
    print(s_min, s_max)

def minmaxsum(arr):
    maxx = max(arr)
    minn = min(arr)
    print(sum(arr) - maxx, sum(arr)- minn)
    

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
    minmaxsum(arr)



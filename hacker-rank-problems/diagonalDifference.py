
import math
import os
import random
import re
import sys


def diagonalDifference(arr):
    diagonal = 0
    anti_diagonal = 0
    for i in range(len(arr)):
        diagonal = diagonal + arr[i][i]
        anti_diagonal += arr[i][len(arr)-1-i]
               
    return abs(diagonal - anti_diagonal)       


if __name__ == '__main__':

    n = int(input().strip())
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))
    result = diagonalDifference(arr)
    print(result)
import math
import os
import random
import re
import sys

def birthdayCakeCandles(candles):
    my_dict = {}
    for i in candles:
        
        if i not in my_dict.keys():
            my_dict[i] = 1
            
        else:
            my_dict[i] +=1
            
    return max(my_dict.values())

    
        
if __name__ == '__main__':
    candles_count = int(input().strip())
    candles = list(map(int, input().rstrip().split()))
    result = birthdayCakeCandles(candles)
    print(result)

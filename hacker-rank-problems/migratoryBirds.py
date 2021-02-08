import math
import os
import random
import re
import sys

# Complete the migratoryBirds function below.
def migratoryBirds(arr):
    bird_dict = {}
    val_list = []
    key_list = []
    for k in arr:
        if k not in bird_dict.keys():
            bird_dict[k] = 1
        else:
            bird_dict[k] += 1
            
    for k, v in bird_dict.items():
        key_list.append(k)   
        val_list.append(v)  

    modd = max(bird_dict.values())  
    position = val_list.index(modd)   
    return key_list[position]

  
if __name__ == '__main__':
    
    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    print(result)

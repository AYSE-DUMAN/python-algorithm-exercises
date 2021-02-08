

import os
import sys


#!/bin/python3

import os
import sys

def timeConversion(s):
    time = ""
    splt = s.split(":")


    if  splt[2][2:] == "PM":
        if  int(splt[0]) < 12:
            s_pm = str(int(splt[0]) + 12)
            time = s_pm + ":" + splt[1] + ":" + splt[2][:2]
        else:
            time = splt[0] + ":" + s.split(":")[1] + ":" + splt[2][:2]
    else:
        if splt[0] == "12":
            time = "00" + ":" + splt[1] + ":" + splt[2][:2]
        else:
            time = splt[0] + ":" + splt[1] + ":" + splt[2][:2]

    return time



if __name__ == '__main__':
    
    s = input()

    result = timeConversion(s)
    print(result)


# 19:05:45AM

import os
import sys
#
# Complete the simpleArraySum function below.
#
def simpleArraySum(ar):
    summ = 0

    for i in range(len(ar)):
        summ += ar[i]
    
    return summ       

if __name__ == '__main__':
    
    ar_count = int(input("enter a number:"))

    ar = list(map(int, input().rstrip().split()))

    result = simpleArraySum(ar)
    print(result)



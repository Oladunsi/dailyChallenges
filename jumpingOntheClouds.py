#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):  
 
    jump = 0              # jumper counter
    pivot = max(c)        # pivot == 1
    arrSize = len(c)      # size of array (c)
    count = 0             # safe jump counter
    lastItem = arrSize-1  # last index in the array
    # if the array size is less than 2 return 1, cause first and last item are always safe
    if arrSize <= 2:
        return 1
    else:
        # while array size greater than 2 
        while jump < arrSize:
            jump += 2   # looking at 2 index ahead
            # if index is 0 (safe) then jump to the index and count increases by 1
            if jump < arrSize and c[jump] != pivot: 
                count += 1           
            # if index is 1 (Not safe) then reduce jump to 1 and count increases by 1
            if jump < arrSize and c[jump] == pivot:
                jump -=1     # jump reduced to 1 
                count += 1
            # if we are two steps away from the last index 
            if jump == lastItem-1 and c[lastItem] != pivot:
                jump += 1   # then jump by 1 instead of 2 and 
                count +=1   # count increase by 1
        return count
               
    
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()

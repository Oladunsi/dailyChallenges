#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the equalizeArray function below.
def deletion(item,arr):
    deletedItems = [i for i in arr if i != item]
    count = len(deletedItems)
    return count
    
    
    
    
def equalizeArray(arr):
    countarr = []
    Uniquearr = set(arr)
    for i in Uniquearr:
        countarr.append(deletion(i,arr))
    return min(countarr)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = equalizeArray(arr)

    fptr.write(str(result) + '\n')

    fptr.close()

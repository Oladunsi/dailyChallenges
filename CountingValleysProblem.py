#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def countingValleys(steps, path):
    # Write your code here
    groundLevel = 0
    upwardMovement = 0
    downwardMovement = 0
    valleyCount = 0
    for _ in range(steps):
        if path[_] == "D":
            upwardMovement -= 1
            downwardMovement +=1
        elif path[_] == "U":
            upwardMovement += 1
            downwardMovement -= 1
            if upwardMovement == downwardMovement == groundLevel:
                valleyCount += 1
    return valleyCount

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    fptr.write(str(result) + '\n')

    fptr.close()

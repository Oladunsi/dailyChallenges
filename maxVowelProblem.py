#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'findSubstring' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#
def voewlsOccurrence(word):
    vowels = "aeiou"
    counter = 0
    for i in word:
        if i in vowels:
            counter += 1
    return counter
    
        

def findSubstring(s, k):
    # Write your code here
    
    substringlist = [s[i:k+i] for i in range(len(s)) if len("".join(s[i:k+i].split("\r"))) == k]
   
    for i in substringlist:
        if max(list(map(voewlsOccurrence, i))) == 0:
            print("No match found")
        elif voewlsOccurrence(i) == max(list(map(voewlsOccurrence, substringlist))):
            return i
             
        
                
s = "ugerdii"
#s = "qwrtpgdz"
k = 5
count = 0

result = findSubstring(s, k)

print(result)
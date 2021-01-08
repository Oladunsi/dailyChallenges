from math import sqrt
import re

def isPrime(n):
    for i in range(2, int(sqrt(n)+1)):
        if n % i is 0:
            return False
    return True
def getPrime(num):
    if num >= 2 and isPrime(num):
      return "Prime"
    else:
        return "Not prime"
    
        
T = int(input())
getnumber = re.compile(r"\d+")
getChar = re.compile(r"\W+\w+\W+")

for _ in range(T):
    n = input()
    numobj = list(map(int,getnumber.findall(n)))
    charobj = getChar.findall(n)
    if len(charobj) == 0:
        print(getPrime(numobj[0]))
    else:
        print(getPrime(numobj[0]) + charobj[0])
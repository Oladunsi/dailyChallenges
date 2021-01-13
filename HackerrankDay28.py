#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    N = int(input())
    Names = []
    GmailName = re.compile(r"[a-z]+@gmail\.com$|[a-z]+@[a-z]+gmail\.com$")
    

    for N_itr in range(N):
        try:
            
            firstNameEmailID = input().split(" ")
            firstName = firstNameEmailID[0]
            emailID = firstNameEmailID[1]
            name = GmailName.match(emailID)
            if name:
                Names.append(firstName)
        except Exception as err:
            pass
    #print(sorted(Names))
    for _ in sorted(Names):
        print(_)
        
        
        

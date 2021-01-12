def sumAll(args):
    a,b = args
    counter = 0
    if a < b:
        for i in getRange(a,b):
            counter += i
        return counter

    for i in getRange(b,a):
         counter += i
    return counter



def getRange(a, b, someArr = []):
    
    if a == b:
        someArr.append(b)
        return someArr
        
    someArr.append(a)
    a += 1
    getRange(a,b)
    return someArr
      
ran = sumAll([10,5])
print(ran)

#ran = getRange(1,9)
#print(ran)
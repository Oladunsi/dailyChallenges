import timeit 

def Binary(bank,n):
    
    divisor = n // 2
    remainder = n % 2
    if divisor != 0:
        bank.append(remainder)
        Binary(bank, divisor)
    else:
        bank.append(1)
        return bank

def occurences(arr):
    count = [len("".join(item.split()).strip()) for item in arr]
    return count

        
n  = 500000000
bank = []
starttime = timeit.default_timer()
print("The start time is :",starttime)
binary = Binary(bank,n)
bank = " ".join(map(str,bank[::-1]))
print("The time difference is :", timeit.default_timer() - starttime)

starttime = timeit.default_timer()
print("The start time is :",starttime)
c = bin(n)
print("The time difference is :", timeit.default_timer() - starttime)

b =  bank.split("0")

a = max(occurences(b))


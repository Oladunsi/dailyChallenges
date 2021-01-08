bar = 6
num = [i for i in range(1,bar+1) if bar % i == 0]
counter = 0
for i in num:
    counter += i
print(counter)

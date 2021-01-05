def StairCaseAlgo(num):
    blank = " "

    for i in range(1,num+1):

        print(blank * (num-i) + "#"*i)

stair = int(input("Enter Stairs: "))
StairCaseAlgo(stair)
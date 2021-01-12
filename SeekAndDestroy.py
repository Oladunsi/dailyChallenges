def destroyer(someArr,*args):
    #someArgs = [remuv for remuv in args if remuv in someArgs]
    for i in args:
        newArr = list(filter(lambda x: x != i, someArr))
        someArr = newArr
    print(i,"No more in =>", newArr)
    
destroyer(["possum", "trollo", 12, "safari", "hotdog", 92, 65, "grandma", "bugati", "trojan", "yacht"], "yacht", "possum", "trollo", "safari", "hotdog", "grandma", "bugati", "trojan")
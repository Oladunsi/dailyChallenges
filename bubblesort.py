def bubbleSort(arr=[]):
    if len(self.arr) < 1:
        return self.arr
    firstItem = self.arr[0]
    counter = 0
    left = [i for i in self.arr if i < firstItem]
    middle = [i for i in self.arr if i == firstItem]
    right = [i for i in self.arr if i > firstItem]
    return self.bubbleSort(left) + middle + self.bubbleSort(right)

   
    
a = bubbleSort([4,3,1,2])
print(a)

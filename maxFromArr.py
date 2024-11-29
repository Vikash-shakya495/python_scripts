def maxArr(n):
    return max(n)

n = int(input("enter the size of the array"))

array = []
for i in range(n):
    array.append(int(input("enter the element")))
    
maxEle = maxArr(array)
print("the maximum element in the array is",maxEle)    
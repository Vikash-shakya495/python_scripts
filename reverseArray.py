def reverseArr(n):
    return n[::-1]
n = int(input("enter the size of the array"))

array=[]
for _ in range(0,n):
    array.append(int(input("enter the element")))
    
newArr = reverseArr(array)
print("The reverse array is :", newArr)    
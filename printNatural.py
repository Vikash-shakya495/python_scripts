def reverseArr(n):
    return n[::-1]

arr=[]
for i in range(1,10):
    arr.append(i)

print("Normal Array", arr)
reversedArr = reverseArr(arr)
print("Reversed Array", reversedArr)
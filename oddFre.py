def checkOdd(n):
    # arr1 = []
    freq = 0
    for i in range(len(n)):
        if n[i] % 2 == 1:
            # arr1.append(n[i])
            freq += 1
    return freq

n = int(input("Enter the size of array"))

array = []
for i in range(n):
    array.append(int(input()))
    
newArr = checkOdd(array)
print("The check odd is", newArr)    
    
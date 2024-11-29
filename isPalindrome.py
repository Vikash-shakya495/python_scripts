def isPalindrome(n):
    return n[::-1]

n = int(input("enter the size of the array"))
arr = []
for i in range(0,n):
    arr.append(int(input()))
    
print("Normal Array", arr)
isPalin = isPalindrome(arr)
if(isPalin == arr):
    print(True)
else:
    print(False)
def isPalindrome(arr,start ,end):
    if start>= end:
        return True
    if arr[start] != arr[end]:
        return False
    return isPalindrome(arr,start+1,end-1)

n = int(input("enter the size of the array"))
arr = []
for i in range(0,n):
    arr.append(int(input()))
    
isPalin = isPalindrome(arr,0,n-1)
print(isPalin)
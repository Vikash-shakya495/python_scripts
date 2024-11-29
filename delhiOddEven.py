def checkOddEven(n):
    for i in range(0,len(n)):
        if n[i] % 4 == 0:
            print("Yes")
        elif n[i] % 3 == 0:
            print("Yes")
        else:
            print("No")

n = int(input("enter no. of Car you want to enter"))

arr =[]
for i in range(n):
    arr.append(int(input("enter car Number")))
    
CanRun = checkOddEven(arr)
# print("This Car can be run",CanRun)    
    
    
def find_the_element(n,ele):
    for i in range(0,len(n)):
        if n[i] == ele:
            return i
        else:
            return -1
n = int(input("enter the size of the array"))

array = []
for i in range(0,n):
    array.append(int(input("enter the element")))
    
print("the element you want to find")   
ele = int(input())

findEle = find_the_element(array,ele)
if findEle != -1 :
    print("The element is at index",findEle)
else:
    print("The element is not in the array")
def odd_even_array(n):
    arr=[]
    for i in range(n-1,0,-1):
        if i%2==1:
            arr.append(i)
    for i in range(1,n):
        if i%2==0:
            arr.append(i)
    return arr        
n = int(input())
result = odd_even_array(n)
print(*result)

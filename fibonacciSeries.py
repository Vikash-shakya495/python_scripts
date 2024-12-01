def fibonacci_series(n):
    a = 0
    b = 1
    for _ in range(2,n+1):
        a, b = b, a+b
    
    return b

n=int(input())
print(fibonacci_series(n))    
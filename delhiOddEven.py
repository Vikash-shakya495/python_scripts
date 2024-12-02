N = int(input())
for _ in range(N):  
    digits = list(map(int, input().strip()))
    even_sum, odd_sum = sum(d for d in digits if d % 2 == 0), sum(d for d in digits if d % 2 != 0)
    print("Yes" if even_sum % 4 == 0 or odd_sum % 3 == 0 else "No")

def abs_even_odd_diff(A):
    even_count = 0 ;
    odd_count = 0;

    for num in A:
        if num % 2==0:
            even_count += 1
        else:
            odd_count += 1
    return even_count - odd_count



a = [1,2,3,4,5,6,7,8]
result = abs_even_odd_diff(a)
print(result)
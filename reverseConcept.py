def reverse_array(n):  
    return n[::-1]

n = int(input("enter the size of the array"))

array = []
for _ in range(n):
    array.append(int(input()))
    

reverse_arr = reverse_array(array)
print(reverse_arr)  
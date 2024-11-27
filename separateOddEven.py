a = [1,2,3,4,5]
odd = []
even = []
for i in range(0,len(a)):
    if(a[i] % 2==0):
        even.append(a[i])
    else:
        odd.append(a[i])
print(odd)
print(even)            
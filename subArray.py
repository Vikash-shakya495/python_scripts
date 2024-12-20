def subarrays(arr):
    n = len(arr)
    result = []
    for i in range(n):
        for j in range(i+1, n + 1):
            result.append(arr[i:j])
        return result

arr = [1,2,3,4,5]
print("Subarrays : " ,subarrays(arr))
        
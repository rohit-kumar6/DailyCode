def findSmallest(arr, n):
    res = 1  # Initialize result
    for i in range(0, n):
        if arr[i] <= res:
            res = res + arr[i]
        else:
            break
    return res


arr1 = [1, 3, 4, 5]
n1 = len(arr1)
print(findSmallest(arr1, n1))


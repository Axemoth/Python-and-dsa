def sum(arr):
    result = 0
    for num in arr:
        result += num
    return result

arr = list(map(int,input("Enter your array:").split()))

print(sum(arr))


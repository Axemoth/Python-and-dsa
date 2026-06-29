
arr = list(map(int,input().split()))
k = int(input())

k = k%len(arr)

arr = arr[-k:] + arr[:-k]
print(len(arr))
print(*arr)
'''

def reverse(arr, start, end):
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1


n = int(input())
arr = list(map(int, input().split()))
k = int(input())

k = k % n

# Reverse whole array
reverse(arr, 0, n - 1)

# Reverse first k elements
reverse(arr, 0, k - 1)

# Reverse remaining elements
reverse(arr, k, n - 1)

print(*arr)
'''
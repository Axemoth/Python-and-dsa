arr = list(map(int, input().split()))

result = []

# Store all non-zero elements
for num in arr:
    if num != 0:
        result.append(num)

# Count zeros
zeros = arr.count(0)

# Append zeros at the end
for i in range(zeros):
    result.append(0)

print(*result)
######################################################################################
arr = list(map(int, input().split()))

# j points to the position where the next non-zero element should go
j = 0

# i scans every element
for i in range(len(arr)):

    # If current element is non-zero
    if arr[i] != 0:

        # Swap current element with the element at index j
        arr[i], arr[j] = arr[j], arr[i]

        # Move j to the next position
        j += 1

print(*arr)
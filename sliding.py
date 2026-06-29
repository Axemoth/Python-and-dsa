n = int(input())
arr = list(map(int,input().split()))

k = int(input())

current_sum = sum(arr[:k])
max_sum = current_sum

for num in range(k,n):
    current_sum = current_sum - arr[k-num] + arr[num]
    
    if current_sum > max_sum:
        max_sum = current_sum
    
print(max_sum)
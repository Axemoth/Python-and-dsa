'''
Find the K-length contiguous subarray with the largest sum
Given an integer array and a window size k, find the maximum sum among all contiguous subarrays of length k.


'''
def subarray(arr,k):
    window_sum = sum(arr[:k])

    max_sum = window_sum

    for j in range(k,len(arr)):
        window_sum += arr[j]

        window_sum -= arr[j-k]

        max_sum = max(max_sum,window_sum)

    return max_sum

arr = list(map(int,input("Enter arr").split()))
k = int(input())

print(subarray(arr,k))
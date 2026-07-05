'''
Sorted input · find indices that add up to target
Given a 1-indexed array of integers sorted in non-decreasing order, return the indices of the two numbers that add up to a given target.
Exactly one solution exists, and you may not use the same element twice.
'''

def twosum(arr,target):
    i = 0
    j = len(arr)-1
    curr_sum = 0
    while i<j:
        curr_sum= arr[i] + arr[j]
        if curr_sum == target:
            return [i+1,j+1]
        
        elif curr_sum>target:
            j-=1
        else :
            i+=1
    
    return []

arr = list(map(int,input().split()))
target = 69

print(twosum(arr,target))
            




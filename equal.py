def equal(arr):
    left_sum = 0
    total = sum(arr)
    for num in arr:
        right_sum = total - num - left_sum
        
        if left_sum == right_sum:
            return True
        left_sum += num
    
    return False
    
arr = list(map(int,input("Enter arr:").split()))

print(equal(arr))
            
    
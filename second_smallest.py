def small(arr):
    bsmall = float('inf')
    csmall = float('inf')
    
    for num in arr:
        if num<bsmall:
            csmall = bsmall
            bsmall = num
            
        elif bsmall < num < csmall:
            csmall = num
    
    return [bsmall,csmall]
    
arr = list(map(int,input("Enter:").split()))

print(small(arr))
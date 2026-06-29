def stock(arr):
    buy = arr[0]
    max_profit = 0
    
    for i in range(1,len(arr)):
        if arr[i] < buy:
            buy = arr[i]
        
        profit = arr[i] - buy
        
        max_profit = max(profit,max_profit)
    
    return max_profit
   
   
arr = list(map(int,input("Enter arr:").split()))

print(stock(arr))
            
    
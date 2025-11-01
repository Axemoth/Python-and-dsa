def two_sum(arr: list[int],target:int) -> list[int]:
    mpp={}
    
    for i,num in enumerate(arr):
        complement = target - num
        if complement in mpp:
            return [mpp[complement],i]
        mpp[num] = i
    return []
    
arr = [int(x) for x in input("Enter your list").split()]
target = int(input("Enter your target"))



res = two_sum(arr,target)
print(" , ".join(map(str,res)))
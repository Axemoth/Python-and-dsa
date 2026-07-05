def twosum(arr,target):
    mpp = {}
    for num in range(len(arr)):
        complement = target - arr[num]
        if complement in mpp:
            return [mpp[complement],num]
        mpp[arr[num]] = num

    return []

arr = list(map(int,input().split()))
target = int(input())

print(twosum(arr,target))
def subset(arr1,arr2):
    result = []
    for i in range(len(arr1)):
        for j in range(len(arr2)):
            if arr2[j] == arr1[i]:
                result.append(arr2[j])
    
    return result
    

arr1 = list(map(int,input("Enter arr1:").split()))
arr2 = list(map(int,input("Enter arr2:").split()))

print(subset(arr1,arr2))
            
    
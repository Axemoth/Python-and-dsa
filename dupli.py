def dupli(s1):
    mpp = {}
    s2 = ""
    for char in s1:
        if char in mpp:
            mpp[char] += 1
        else:
            mpp[char] = 1
    
    for i in mpp:
        s2 += i
        
    return s2

s1 = input()

print(dupli(s1))
    
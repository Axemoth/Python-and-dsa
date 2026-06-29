def rep(s1):
    mpp = {}
    for char in s1:
        if char in mpp:
            mpp[char] += 1
        else:
            mpp[char] = 1
    print(mpp)
    for i in mpp:
        if mpp[i] == 1:
            return i
    return -1

s1 = input()
print(rep(s1))
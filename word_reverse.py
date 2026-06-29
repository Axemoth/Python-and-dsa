def rev(s1):
    words = s1.split()
    result = []
    for word in words:
        result.append(word[::-1])
    
    return " ".join(result)
        
    
s1 = input()
print(rev(s1))
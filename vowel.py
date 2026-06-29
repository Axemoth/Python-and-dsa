def vowel(s1):
    v = 0
    c = 0
    vowel = ['a','e','i','o','u']
    for char in s1.lower():
        if char.isalpha():
            
            if char in vowel:
                v += 1
            else:
                c += 1
    
    return (v,c)

s1 = input()
print(vowel(s1))
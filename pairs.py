n = int(input("Enter number of pairs to sort"))
pairs = [] 
for _ in range(n):
     x,y = map(int,input("Enter pair:").split())
     pairs.append((x,y))
     
     pairs.sort(key = lambda p:(p[0],p[1]))
     
for x,y in pairs:
    print(x,y)
     
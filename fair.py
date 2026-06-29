n = int(input())
fair = 0
for i in range(n):
    if n <=2:
        fair +=100
    if n>2 and n<=5:
        fair +=50
    if n>5:
        fair +=20
        
print(fair)
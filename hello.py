print("helloworld")
l1 = [1,2,3,'p']
l2=l1
l2[0]=69
print(l2)
print(l1)
if l2==l1:
    print("equal")
else:
    print("not equal")
x=10
y=x
y=20
print(x)
print(y)
#reassignment creates a new object in memory for immutable types
#but for mutable types it just creates a new reference to the same object in memory
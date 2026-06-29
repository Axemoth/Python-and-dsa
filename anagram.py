s1 = input()
s2 = input()
if len(s1) != len(s2):
    print("Non matched")
mpp1 = {}
mpp2={}

for i  in s1:
    if i in mpp1:
        mpp1[i] +=1
    else:
        mpp1[i] = 1

for j in s2:
    if j in mpp2:
        mpp2[j] +=1
    else:
        mpp2[j] = 1
        
if mpp1 == mpp2:
     print("MATCHED")
else:
    print("NOT MATCHED")



        
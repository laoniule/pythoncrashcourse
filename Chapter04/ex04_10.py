#!/usr/bin/python
threetimeslist=[]
for k in range(1,21):
    if k%3==0:
        threetimeslist.append(k)

for m in threetimeslist[0:3]:
    print("The first three items in the list are:",m) 

x=int(len(threetimeslist)/2-1)
y=int(len(threetimeslist)/2+2)   
print(x)
print(y)
for m in threetimeslist[x:y]:
    print("The middle three items in the list are:",m)     

for m in threetimeslist[-3:]:
    print("The last three items in the list are:",m) 

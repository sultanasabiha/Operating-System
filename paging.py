
ms=int(input("Enter the memory size -- "))
ps=int(input("Enter the page size -- "))

nop = ms//ps
print("The no. of pages available in memory are --",nop)

np=int(input("Enter number of processes -- "))
s=[0]*np
fno=[]
rempages = nop
for i in range(np):
    print("Enter no. of pages required for P",i," -- ")
    s[i]=int(input())

    if(s[i] >rempages):
        print("\nMemory is Full")
        break

    rempages = rempages - s[i]
    v=[]
    print("Enter pagetable for P",i," -- ")
    for j in range(s[i]):
        v.append(int(input()))
    fno.append(v)

print(fno)

print("\nLogical Address to find Physical Address:")
pn,pgn,off=[int(x) for x in (input("Enter process no. and pagenumber and offset (x y z) -- ").split())]

if(pn>np or pgn>=s[pn] or off>=ps):
    print("Invalid Input")

else:
    pa=fno[pn][pgn]*ps+off
    print("The Physical Address is --",pa)



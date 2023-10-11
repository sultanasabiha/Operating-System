import random
ds=int(input("Enter Disk Size(in kb):"))
bs=int(input("Enter Block Size(in bytes):"))
nbs=ds*1024//bs
print("\nTotal no. of blocks:",nbs)
db=[-1]*nbs
n=int(input("\nEnter no. of files:"))
fs=[0]*n
ib=[0]*n

blocks=[]
for i in range(n):
    print("Enter file",i,"size(in kb):")
    fs[i]=int(input())
    print("Enter Index Block of file",i)
    ib[i]=int(input())
    db[ib[i]]=0


for i in range(n):
    v=[]
    c=0
    try:
        while c!=(fs[i]*1024)//bs:
            val=random.randint(0,nbs-1)
            if db[val]==-1:
                db[val]=0
                v.append(val)
                c+=1
        blocks.append(v)
    except:
        print("File cannot be allocated")
print("\nFile\tIndex\tNBlocks\t\tBlocks Allocated")
for i in range(n):
    print(i,"\t",ib[i],"\t",(fs[i]*1024)//bs,"\t",blocks[i])
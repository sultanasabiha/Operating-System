import random
ds=int(input("Enter Disk Size(in kb):"))
bs=int(input("Enter Block Size(in bytes):"))
nbs=ds*1024//bs
print("\nTotal no. of blocks:",nbs)
db=[-1]*nbs
n=int(input("\nEnter no. of files:"))
fs=[0]*n
sb=[0]*n
eb=[0]*n

blocks=[]
for i in range(n):
    print("Enter file",i,"size(in kb):")
    fs[i]=int(input())
    print("Enter Starting Block of file",i)
    sb[i]=int(input())
    print("Enter Ending Block of file",i)
    eb[i]=int(input())

for i in range(n):
    v=[]
    v.append(sb[i])
    db[sb[i]]=0
    c=2
    try:
        while c!=(fs[i]*1024)//bs:
            val=random.randint(0,nbs-1)
            if db[val]==-1:
                db[val]=0
                v.append(val)
                c+=1
    except:
        print("File cannot be allocated")
    db[eb[i]]=0
    v.append(eb[i])
    blocks.append(v)

print("\nFile\tStart\tEnd\tNBlocks\t\tBlocks Allocated")
for i in range(n):
    print(i,"\t",sb[i],"\t",eb[i],"\t",(fs[i]*1024)//bs,"\t",blocks[i])
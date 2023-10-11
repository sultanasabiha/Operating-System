n=int(input("Enter no. of files:"))
fs=[0]*n
sb=[0]*n
bs=[0]*n
nbs=[0]*n
blocks=[]
for i in range(n):
    print("Enter file",i,"size(in kb):")
    fs[i]=int(input())
    print("Enter Starting Block of file",i)
    sb[i]=int(input())
    print("Enter blocksize for file",i,"(in bytes):")
    bs[i]=int(input())

for i in range(n):
    nbs[i]=(fs[i]*1024)//bs[i]

for i in range(n):
    v=[]
    for j in range(nbs[i]):
        v.append(sb[i]+j)
    blocks.append(v)

print("\nFile\tStart\tNBlocks\t\tBlocks Allocated")
for i in range(n):
    print(i,"\t",sb[i],"\t",nbs[i],"\t",blocks[i])
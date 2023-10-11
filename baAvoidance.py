n=int(input("Enter the no. of processes:"))
m=int(input("Enter the no. of resources:"))

finish=['n']*n
max=[[0 for j in range(m)] for i in range(n)]
alloc=[[0 for j in range(m)] for i in range(n)]
need=[[0 for j in range(m)] for i in range(n)]
total=[0]*m
avail=[0]*m
work=[0]*m

print("Enter the Claim Matrix:\n")
for i in range(n):
    for j in range(m):
        max[i][j]=int(input())

print("Enter the Allocation Matrix:\n")
for i in range(n):
    for j in range(m):
        alloc[i][j]=int(input())

print("Enter Total instances of the Resources:")
for i in range(m):
    total[i]=int(input())

print("Enter the Available Resource Vector:")
for i in range(m):
    avail[i]=int(input())

work=list(avail)

for i in range(n):
    for j in range(m):
        need[i][j]=max[i][j]-alloc[i][j]

sequence=[]
while('n' in finish):
    for i in range(n):
        c=0
        for j in range(m):
            if((need[i][j]<=work[j]) and (finish[i]=='n')):
                c+=1
        if(c==m):
            print("All the resources can be allocated to Process ", i+1)
            for k in range(m):
                work[k]+=alloc[i][k]
            print("\n\nAvailable resources are:",work)

            finish[i]='y'
            sequence.append(i+1)
c=0
for i in range(m):
    if(work[i]<=total[i]):
        c+=1
if(c==m):
    print("\nSystem is in safe state")
    print("The safe sequence of process execution:\n",sequence)
else:
    print("The System is unsafe, Deadlock might occur!")

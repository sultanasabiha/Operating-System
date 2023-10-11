
n=int(input("Enter no. of processes:"))
bt=[0]*n
wt=[0]*n
tat=[0]*n

for i in range(n):
    print("Enter burst time for process",i)
    bt[i]=(int(input()))
btsorted=sorted(enumerate(bt),key=lambda x:x[1])
#arr.sort(key=lambda x: (x.weight), reverse=True) 
wtavg=0.0
tat[0]=btsorted[0][1]
tatavg=float(btsorted[0][1])

for i in range(1,n):
    wt[i]=wt[i-1]+btsorted[i-1][1]
    tat[i]=tat[i-1]+btsorted[i][1]
    wtavg+=wt[i]
    tatavg+=tat[i]
print("PROCESS\t\tBURST TIME\tWAITING TIME\tTURN AROUND TIME")
for i in range(n):
    print("P",btsorted[i][0],"\t\t",btsorted[i][1],"\t\t",wt[i],"\t\t",tat[i])
print("Average Waiting Time:",wtavg/n)
print("Average Turn Around Time:",tatavg/n)
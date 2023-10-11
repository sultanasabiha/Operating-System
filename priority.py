
n=int(input("Enter no. of processes:"))
bt=[0]*n
wt=[0]*n
tat=[0]*n
pri=[0]*n
for i in range(n):
    print("Enter burst time and priority for process",i,"(x y):")
    bt[i],pri[i]=[int(x) for x in((input().split()))]

bts=[x for _, x in sorted(zip(pri,bt))]
pris=sorted(enumerate(pri),key=lambda x:x[1])
wtavg=0.0
tat[0]=bts[0]
tatavg=float(bts[0])

for i in range(1,n):
    wt[i]=wt[i-1]+bts[i-1]
    tat[i]=tat[i-1]+bts[i]
    wtavg+=wt[i]
    tatavg+=tat[i]
print("PROCESS\t\tPRIORITY\tBURST TIME\tWAITING TIME\tTURN AROUND TIME")
for i in range(n):
    print("P",pris[i][0],"\t\t",pris[i][1],"\t\t",bts[i],"\t\t",wt[i],"\t\t",tat[i])
print("Average Waiting Time:",wtavg/n)
print("Average Turn Around Time:",tatavg/n)
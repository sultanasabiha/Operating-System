
n=int(input("Enter no. of processes:"))
bt=[0]*n
wt=[0]*n
tat=[0]*n

for i in range(n):
    print("Enter burst time for process",i)
    bt[i]=(int(input()))
btc=list(bt)

ts=int(input("Enter the size of time slice:"))
max=max(bt)
temp=0
for j in range((max//ts)+1):
    for i in range(n):
        if(bt[i]!=0):
            if (bt[i]<=ts):
                tat[i]=temp+bt[i]
                temp+=bt[i]
                bt[i]=0
            else:
                bt[i]=bt[i]-ts
                temp+=ts
tatavg=0
wtavg=0
for i in range(n):
    wt[i]=tat[i]-btc[i]
    tatavg+=tat[i]
    wtavg+=wt[i]
print("PROCESS\t\tBURST TIME\tWAITING TIME\tTURN AROUND TIME")
for i in range(n):
    print("P",i,"\t\t",btc[i],"\t\t",wt[i],"\t\t",tat[i])
print("Average Waiting Time:",wtavg/n)
print("Average Turn Around Time:",tatavg/n)

n=int(input("Enter no. of processes:"))
bt=[0]*n
wt=[0]*n
tat=[0]*n


for i in range(n):
    print("Enter burst time for process",i)
    bt[i]=(int(input()))
wtavg=0.0
tat[0]=bt[0]
tatavg=float(bt[0])

for i in range(1,n):
    wt[i]=wt[i-1]+bt[i-1]
    tat[i]=tat[i-1]+bt[i]
    wtavg+=wt[i]
    tatavg+=tat[i]
print("PROCESS\t\tBURST TIME\tWAITING TIME\tTURN AROUND TIME")
for i in range(n):
    print("P",i,"\t\t",bt[i],"\t\t",wt[i],"\t\t",tat[i])
print("Average Waiting Time:",wtavg/n)
print("Average Turn Around Time:",tatavg/n)
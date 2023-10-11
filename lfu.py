print("Enter the number of frames: ",end="")
capacity = int(input())
f,fault,pf,top = [],0,'No',0
st=dict()

print("Enter the reference string: ",end="")
s = list(map(int,input().strip().split()))
print("\nString|Frame \t",end='')
for i in range(capacity):
    print(i,end=' ')
print("Fault\n   \n")
for i in s:
    if i not in f:
        if len(f)<capacity:
            f.append(i)
            if i not in st.keys():
                st[i]=1
            else:
                '''v=st[i]+1
                del s[i]            //LRU
                st[i]=v'''
                st[i]+=1
        else:
            m=st.get(f[0])    
            for v in f:
                if m>st.get(v):
                    m=st.get(v)
            iterate=list(st.keys())

            for k in iterate:
                if k in f and st[k]==m :
                    f[f.index(k)]=i
                    if i not in st.keys():
                        st[i]=1
                    else:
                        '''
                        v=st[i]+1
                        del st[i]       LRU
                        st[i]=v
                        '''
                        st[i]+=1
                    break
            
        pf = 'Yes'
        fault += 1
    else:
        pf = 'No'
        '''v=st[i]+1
        del st[i]           LRU
        st[i]=v'''
        st[i]+=1
    print("   %d\t\t"%i,end='')
    for x in f:
        print(x,end=' ')
    for x in range(capacity-len(f)):
        print(' ',end=' ')
    print(" %s"%pf)
print("\nTotal Requests: %d\nTotal Page Faults: %d\nFault Rate: %0.2f%%"%(len(s),fault,(fault/len(s))*100))


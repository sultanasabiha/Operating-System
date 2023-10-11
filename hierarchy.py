import os
import fnmatch
'''
wpath=input(("\nEnter path of working directory -- "))
os.chdir(wpath)
'''
rn=int(input("Enter no. of root directories:"))
root=['']*rn
for i in range(rn):
    root[i]=input("Enter directory name:") 
    os.chdir("/")
    os.mkdir(root[i])
os.chdir("/")
while(True):
    if os.getcwd()=="C:\\":
        print("\n\n----------OPTIONS----------\n")
        for i in range(rn):
            print(i+1,". Open",root[i])
        r=int(input("Enter your choice -- "))-1
        os.chdir(root[r])
        print(root[r],"is opened.")
    print("\n\n----------OPTIONS----------\n1. Create Directory\n2. Delete Directory\n3. Open Directory\n4. Display Files and Directories\n5. Search File or Directory\n6. Create File\n7. Delete File\n8. Go back to previous directory\n9. Exit\nEnter your choice -- ")
    ch=int(input())
    match ch:
        case 1: 
            di=input(("\nEnter the name of the directory -- "))
            di=os.getcwd()+"\\"+di
            os.mkdir(di)
            print("Directory Created.")
        case 2:
            dd=input(("\nEnter the name of the directory -- "))
            dd=os.getcwd()+"\\"+dd
            os.rmdir(dd)
            print("Directory Deleted.")
        case 3:
            do=input(("\nEnter the name of the directory -- "))
            do=os.getcwd()+"\\"+do
            os.chdir(do)
            print("Directory Opened.")
        case 6: 
            fn=input(("\nEnter the name of the file -- "))
            f=open(fn,"w+")
            print("File is Created.")
        case 7:
            fn=input(("\nEnter the name of the file -- "))
            os.remove(fn)
            print("File is Deleted.")
        case 5:
            fn=input("\nEnter the name of the file or directory -- ")
            if fn in os.listdir(os.getcwd()):
                print(fn,"is found.")
            else:
                print("File or folder not found!")
        case 4:
            print("Files an directories in the directory --")
            for entry in os.listdir(os.getcwd()):
                print(entry)
        case 8:
            os.chdir("../") 
        case 9:
            exit()

        case default:
            print("\nInvalid Input!")

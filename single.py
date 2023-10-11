import os
import fnmatch

#wpath=input(("\nEnter path of working directory -- "))
#os.chdir(wpath)

wpath=input(("\nEnter name of working directory -- "))
os.mkdir(wpath)
os.chdir(wpath)
'''
print("--Root is the working directory--")
wpath="/"
os.chdir(wpath)
'''
while(True):
    print("\n----------OPTIONS----------\n1. Create File\n2. Delete File\n3. Search File \n4. Display Files\n5. Exit\nEnter your choice -- ")
    ch=int(input())
    match ch:
        case 1: 
            fn=input(("\nEnter the name of the file -- "))
            f=open(fn,"x")
            print("Files is Created.")
        case 2:
            fn=input(("\nEnter the name of the file -- "))
            os.remove(fn)
            print("Files is Deleted.")
        case 3:
            fn=input(("\nEnter the name of the file -- "))
            c=0
            for f in os.listdir(wpath):
                if fnmatch.fnmatch(f,fn):
                    print(f,"is found.")
                    c=1
            if(c==0):
                print("File is not found!")
        case 4:
            print("Files in the directory --")
            for entry in os.listdir(wpath):
                if os.path.isfile(os.path.join(wpath, entry)):
                    print(entry)
        case 5:
            exit()
        case default:
            print("\nInvalid Input!")

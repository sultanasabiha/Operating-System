import os
import fnmatch
'''
wpath=input(("\nEnter path of working directory -- "))
os.chdir(wpath)
'''
wpath=input(("\nEnter name of Master directory -- "))
os.mkdir(wpath)
#print("--Root is the master directory--")
#wpath="/"
os.chdir(wpath)
while(True):
    print("\n\n----------OPTIONS----------\n1. Create Directory\n2. Delete Directory\n3. Open Directory\n4. Display Directories\n5. Search Directory\n6. Exit\nEnter your choice -- ")
    ch=int(input())
    match ch:
        case 1: 
            di=input(("\nEnter the name of the directory -- "))
            di=wpath+"\\"+di
            os.mkdir(di)
            print("Directory Created.")
        case 2:
            dd=input(("\nEnter the name of the directory -- "))
            dd=wpath+"\\"+dd
            os.rmdir(dd)
            print("Directory Deleted.")
        case 3:
            do=input(("\nEnter the name of the directory -- "))
            do=wpath+"\\"+do
            os.chdir(do)
            print("Directory Opened --")
            while(True):
                print("\n\n----------OPTIONS----------\n1. Create File\n2. Delete File\n3. Search File \n4. Display Files\n5. Go back to previous directory\n6. Exit\nEnter your choice -- ")
                ch2=int(input())
                match ch2:
                    case 1: 
                        fn=input(("\nEnter the name of the file -- "))
                        f=open(fn,"x")
                        print("File is Created.")
                    case 2:
                        fn=input(("\nEnter the name of the file -- "))
                        os.remove(fn)
                        print("File is Deleted.")
                    case 3:
                        fn=input("\nEnter the name of the file -- ")
                        if fn in os.listdir(os.getcwd()):
                            print(fn,"is found.")
                        else:
                            print("File not found!")
                    case 4:
                        print("Files in the directory --")
                        for entry in os.listdir(do):
                            print(entry)
                    case 5:
                        os.chdir(wpath) 
                        break
                    case 6:
                        exit()
                    case default:
                        print("\nInvalid Input!")
        case 4:
            print("Folders in the directory --")
            for entry in os.listdir(wpath):
                print(entry)
        case 5:
            fn=input(("\nEnter the name of the directory-- "))
            if fn in os.listdir(os.getcwd()):
                print(fn,"is found.")
            else:
                print("Directory not found!")
        case 6:
            exit()
        case default:
            print("\nInvalid Input!")

import os

def DirectoryWatcher(directoryName = "Marvellous"):
    
    flag = os.path.isabs(directoryName)
    
    if(flag == False):
        directoryName = os.path.abspath(directoryName)

    flag=os.path.exists(directoryName)

    if(flag==False):
        print("The path is invalid")
        exit()
        
    flag=os.path.isdir(directoryName)
    if flag==False:
        print("path is valid but target it is not dictiory")
        exit()

        
    print("Absolute path is : "+directoryName)
    
    totalcount=0
    emptycount=0

    for FolderName , SubFolderNames, FileNames in os.walk(directoryName):
        for fname in FileNames:
            totalcount=totalcount+1

            if(os.path.getsize(os.path.join(FolderName,fname))==0):
                emptycount=emptycount+1
                print("File name is "+fname)
                os.remove(os.path.join(FolderName,fname))
        
    print("Toala no of files scan :",totalcount)     
    print("Toala files of deleted scan :",emptycount)     

def main():
    DirName = input("Enter the name of directory that you want to travel : ")
    
    DirectoryWatcher(DirName)
            
    
if __name__ == "__main__":
    main()
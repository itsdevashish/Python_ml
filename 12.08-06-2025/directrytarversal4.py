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
    
    for FolderName , SubFolderNames, FileNames in os.walk(directoryName):
        print("Folder name is : "+FolderName)
        
        for subf in SubFolderNames:
            print("SubFolder name is "+subf)
            
        for fname in FileNames:
            print("File name is "+fname)

def main():
    DirName = input("Enter the name of directory that you want to travel : ")
    
    DirectoryWatcher(DirName)
            
    
if __name__ == "__main__":
    main()
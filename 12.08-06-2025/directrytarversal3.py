import os

def dictorywathcher(dictoryname):
    for FolderName , SubFolderNames, FileNames in os.walk(dictoryname):
        print("Folder name is : "+FolderName)
        
        for subf in SubFolderNames:
            print("SubFolder name is "+subf)
            
        for fname in FileNames:
            print("File name is "+fname)

def main():
    print("Enter the name of dictiory what you want to travel")
    dirname=input()
    dictorywathcher(dirname)

if __name__ == "__main__":
    main()
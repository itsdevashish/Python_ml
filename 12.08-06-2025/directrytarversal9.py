import os
import sys

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
    border = "-"*54
    print(border)
    print("----------------------Marvellous Automation---------------------")
    print(border)

    if (len(sys.argv)==2):
        if((sys.argv[1]=="--h")or((sys.argv[1]=="--H")) ):
            print("This application is used perform directory cleaning" )
            print("This is the automation script")

        elif((sys.argv[1]=="--u")or((sys.argv[1]=="--U")) ):
            print("use the given script as")
            print("scriptname.py nameofdirectory")
            print("Please provide valid absolute path")
        else:
            DirectoryWatcher(sys.argv[1])

    

    else:
        print("Invalid number of command line arguments")   
        print("use the given flag as :")
        print("--h: used to display the help")
        print("--u: used to display the uages")


    print(border)
    print("---------------Thank you for using our sctipt-------------------")
    print("-------------------Marvellous infosystems-----------------------")
    print(border)


            
    
if __name__ == "__main__":
    main()
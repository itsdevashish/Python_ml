import os

def main():
    print("Enter the name of directory")
    dirname=input()

    ret=os.path.isabs(dirname)
    
    if(ret==True):
        print("Input is absolute path")
    else:
        print("Input is relative path")
        newpath=os.path.abspath(dirname)
        print("updated path is :",newpath)

if __name__ == "__main__":
    main()
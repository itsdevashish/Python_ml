import os

def main():
    print("Enter the name of file that you want to read")
    filename=input()

    ret=os.path.exists(filename)
    if (ret==True):
        print ("File is present in the current directory")
        fobj=open(filename,"r")
        data=fobj.read()

        print("Data from file is :",data)

        fobj.close() 
         
    else:
        print ("There is such a no file")
    
if __name__ == "__main__":
    main()
import os

def main():
    print("Enter the name of file that you want to delete")
    filename=input()

    ret=os.path.exists(filename)
    if (ret==True):
        print ("File is present in the current directory")
        os.remove(filename)
         
    else:
        print ("There is such a no file")
    
if __name__ == "__main__":
    main()
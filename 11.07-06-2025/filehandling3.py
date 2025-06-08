def main():
    print("Enter the name of file that you want to create")
    filename=input()

    fobj=open(filename,"w")
    print("Enter the data you want to write into the file")
    
    data=input()
    fobj.write(data)

    fobj.close()
    

if __name__ == "__main__":
    main()
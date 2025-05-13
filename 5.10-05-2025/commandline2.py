import sys

def main():
    print("Number of command line arguments are : ",len(sys.argv))
    print("The Datatype of argv is :",type(sys.argv))
    print("First Command line argument is : ",sys.argv[0])
    print("Second Command line argument is : ",sys.argv[1])
    print("Third Command line argument is :",sys.argv[2])
    print("Fourth Command line argument is : ",sys.argv[3])
if __name__ == "__main__":
    main()
import sys

def main():
    print("Number of command line arguments are : ",len(sys.argv))
    
    print("List of Coomandline arguments are : ->")

    for value in sys.argv:
        print(value)

if __name__ == "__main__":
    main()
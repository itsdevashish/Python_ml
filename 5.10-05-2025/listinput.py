def main():
    print("Enter no of elemnets")
    size=int(input())

    data=list()

    print("Enter The values :")

    for i in range(size):
        no=int(input())
        data.append(no)
    
    print("Entered elements are :")

    for value in data:
        print(value)



if __name__ == "__main__":
    main()
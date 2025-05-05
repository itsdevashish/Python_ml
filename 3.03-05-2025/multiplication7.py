def multiplication(value1,value2):
    result=value1*value2
    return result

def main():
    print("Enter First Number :")
    no1=int(input())

    print("Enter Second Number :")
    no2=int(input())

    ans=multiplication(no1,no2)

    print("The Multiplication is :",ans)

if __name__== "__main__":
    main()

def addition(a,b):
    result =a+b
    return result

def main():
    print("Enter first number")
    no1=int(input())

    print("Enter Second number")
    no2=int(input())

    ret=addition(no1,no2)
    print("The Addition is :",ret)

if __name__ == "__main__":
    main()

def main():
    print("Enter 1st no")
    no1=int(input())

    print("Enter 2nd no")
    no2=int(input())
    
    ans=0

    try:
        ans=no1/no2
    
    except ZeroDivisionError:
        print("Exception ocurred due to second input")

    print ("The Division is:",ans)

if __name__ == "__main__" :
    main()

def calculatepercentage(Total,Obtained):
    output=((Obtained/Total)*100)
    return output

def main():
    print ("Enter Total marks")
    value1=int(input())

    print ("Enter Obtained marks")
    value2=int(input())

    result=calculatepercentage(Obtained=value2,Total=value1) #keyword arguments

    print("Percentage is : ",result)

if __name__ == "__main__" :
    main()
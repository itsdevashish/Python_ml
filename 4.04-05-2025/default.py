def calculatepercentage(Obtained,Total=500):
    output=((Obtained/Total)*100)
    return output

def main():

    print ("Enter Obtained marks")
    value2=int(input())

    result=calculatepercentage(value2) #default arguments

    print("Percentage is : ",result)

if __name__ == "__main__" :
    main()
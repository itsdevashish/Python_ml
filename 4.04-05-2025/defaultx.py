#Multiple Default Argument
def calculatepercentage(Obtained=400,Total=500):
    output=((Obtained/Total)*100)
    return output

def main():

    result=calculatepercentage(350,450) 
    print("Percentage is : ",result)

    result=calculatepercentage(350)
    print("Percentage is : ",result)

    result=calculatepercentage() 
    print("Percentage is : ",result)

if __name__ == "__main__" :
    main()
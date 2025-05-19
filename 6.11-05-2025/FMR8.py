checkeven = lambda no : (no%2 == 0)
increase = lambda no: no+1
sum = lambda a,b : a+b

def filterX(Task, Values):
    Result = []

    for no in Values:
        Ret = Task(no)
        if(Ret == True):
            Result.append(no)
    
    return Result

def mapX(Task, Values):
    Result = []

    for no in Values:
        Ret = Task(no)
        Result.append(Ret)

    return Result

def reduceX(Task, Values):
    Result = 0

    #   [11, 13, 5, 7, 9, 13, 17]
    for no in Values:
        Result = Task(Result,no)

    return Result

def main():
    Data = []
    
    print("Enter number of elements : ")
    Size = int(input())

    print("Please enter numeric values : ")
    for i in range(Size):
        no = int(input())
        Data.append(no)

    print("Input data : ",Data)

    FData = list(filterX(checkeven,Data))
    print("Filter output : ",FData)

    MData = list(mapX(increase,FData))
    print("map output : ",MData)

    RData = reduceX(sum,MData)
    print("reduce output : ",RData)

if __name__ == "__main__":
    main()
checkeven = lambda no : (no%2 == 0)
increase = lambda no: no+1
sum = lambda a,b : a+b

from MarvellousFMR import filterX, mapX, reduceX

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
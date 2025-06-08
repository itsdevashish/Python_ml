class arithmetic:

    def __init__(self,a,b):
        self.no1=a
        self.no2=b

    def addition(self):
        result=0
        result=self.no1+self.no2
        return result
    

def main():
    print("Enter first number")
    value1=int(input())

    print("Enter Second number")
    value2=int(input())

    obj=arithmetic(value1,value2)
    ret=obj.addition()

    print("The Addition is :",ret)

if __name__ == "__main__":
    main()
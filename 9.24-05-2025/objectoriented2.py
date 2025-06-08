class arithmetic:

    def __init__(self,a,b):
        print("Inside Constructor")
        self.no1=a
        self.no2=b

    def addition(self):
        result=0
        result=self.no1+self.no2
        return result
    
    def __del__(self):
        print("Inside Destructor")
    

def main():
    obj1=arithmetic(10,11)
    obj2=arithmetic(20,21)

    ret= obj1.addition()
    print("The additio is",ret)

    ret= obj2.addition()
    print("The additio is",ret)

if __name__ == "__main__":
    main()
class employee():
    Companyname="Marvellous" #-> classvaribale

    def __init__(self,a,b,c): #-> constructor
        print("Inside Constructor")
        self.name = a #-> instance variable
        self.salary = b #-> instance variable
        self.city = c #-> instance variable

    def __del__(self): #-> destructor
        print("Inside Destructor")
    

    def Displayinfo(self):#->Instance Method
        print("Inisde Instance method Displayinfo")
        print("Employee Name :"+self.name)
        print("Employee Salary :",self.salary)   
        print("Employee City :"+self.city)

    @classmethod #->decoreter
    def DisplayCompanyDetails(cls): #->class Method
        print("Inside class methodDisplayCompanydetails ")
        print("Company name :"+cls.Companyname)

    @staticmethod #->decoreter
    def displaycompanypolicy():
        print("Inside static method")
        print("All empolyees are 18+")
        print("Working ours 9 to 6 ")
        print("Holidays : saturday and sunday")


def main():
    print("Class Varibale is :"+ employee.Companyname)
    employee.DisplayCompanyDetails()

    emp1=employee('Rahul',15000,'Pune') #-> object creation
    emp2=employee('Pooja',25000,'Mumbai') #-> object creation
    
    print("Employee Name :"+emp1.name)
    print("Employee Salary :",emp1.salary)   
    print("Employee City :"+emp1.city)

    emp2.Displayinfo()
    employee.displaycompanypolicy()
    del emp1
    del emp2


if __name__ == "__main__":
    main()
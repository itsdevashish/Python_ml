class employee():
    Companyname="Marvellous" #-> classvaribale

    def __init__(self,a,b,c):
        print("Inside Constructor")
        self.name = a
        self.salary = b
        self.city = c

        
    def __del__(self):
        print("Inside Destructor")

def main():
    print("Class Varibale is :"+ employee.Companyname)
    emp1=employee('Rahul',15000,'Pune')
    emp2=employee('Pooja',25000,'Mumbai')
    
    print("Employee Name :"+emp1.name)
    print("Employee Salary :",emp1.salary)   
    print("Employee City :"+emp1.city)



if __name__ == "__main__":
    main()
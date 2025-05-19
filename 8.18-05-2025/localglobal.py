
no=11 #global variable


def fun():
    print("Inside Fun :")
    x=21 #local variable
    print("Value of x is :",x) #21
    print("Value of no : ",no) #11


def sun ():
    print("Inside Sun :")
    y=51 #local variable
    print("Value of y is :",y) #51
    print("Value of no : ",no) #11


def main():
    fun()
    sun()

if __name__=="__main__":
    main()
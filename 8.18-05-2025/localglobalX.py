
no=11 #global variable

def fun():
    global no #global variable
    print("Inside Fun :")
    x=21 #local variable
    print("Value of x is :",x) #21
    no=no+1
    print("Value of no : ",no) #11


def main():
    print("value of no before fun ",no) #11
    fun()
    print("value of no after fun ",no)

if __name__== "__main__" :
    main()
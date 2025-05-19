
no=11 

def fun(no):
    #global no  ---> as karu naka 
    print("fun no :",no) #21

def main():
    print("main no :",no)#11
    fun(21)


if __name__== "__main__" :
    main()
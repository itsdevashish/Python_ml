import sys

def main():
    border = "-"*54
    
    print(border)
    print("----------------------Marvellous Automation---------------------")
    print(border)

    if (len(sys.argv)==2):
        if((sys.argv[1]=="--h")or((sys.argv[1]=="--H")) ):
            print("This application is used to perform --------")
            print("This is the automation script")

        elif((sys.argv[1]=="--u")or((sys.argv[1]=="--U")) ):
            print("use the given script as")
            print("scriptname.py argument1 argument2")
        else:
            print("use the given flag as :")
            print("--h:used to display the help")
            print("--u: used to displau the uages")
    
    else:
        print("Invalid number of command line arguments")   
        print("use the given flag as :")
        print("--h: used to display the help")
        print("--u: used to display the uages")


    print(border)
    print("---------------Thank you for using our sctipt-------------------")
    print("-------------------Marvellous infosystems-----------------------")
    print(border)

if __name__ =="__main__":
    main()
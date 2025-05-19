import threading              # new create->runnable->run->waiting->dead

def display(value1,value2):
    print("Thread id of child is :",threading.get_ident())
    print("Inside Display",value1,value2)
    for i in range(10):
        print(i)

def main():
    print("Inside Main")
    print("Thread id of main is :",threading.get_ident())
    T1=threading.Thread(target=display,args = (11,21))
    T1.start()
    T1.join()
    print("End of main")


if __name__ == "__main__":
    main() 
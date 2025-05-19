import threading              # new create->runnable->run->waiting->dead

def display(value1,value2):
    print("Inside Display",value1,value2)
    for i in range(1000):
        print(i)

def main():
    print("Inside Main")
    T1=threading.Thread(target=display,args = (11,21))
    T1.start()
    print("End of main")


if __name__ == "__main__":
    main() 
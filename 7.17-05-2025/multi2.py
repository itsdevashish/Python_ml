import os

def main():
    print("Pid of current process is :",os.getpid())
    print("Pid of parent process is :",os.getppid())



if __name__ == "__main__":
    main()
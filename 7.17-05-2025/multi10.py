import multiprocessing   
import os          
import multiprocessing.process
import time

def sumeven(no):
    print("Pid of sumeven process  is",os.getpid())
    print("PPid of sumeven process is",os.getppid())
    sum=0
    for i in range(2,no+1,2):
        sum=sum+i
    print(sum)

def sumodd(no):
    print("Pid of sumodd process  is",os.getpid())
    print("PPid of sumodd process is",os.getppid())
    sum=0
    for i in range(1,no+1,2):
        sum=sum+i
    print(sum)


def main():
    print("Demonstratation od parallel execuation")
    print("PID of main process is ",os.getpid())
    start_time=time.time()

    T1=multiprocessing.Process(target=sumeven,args=(900000000,))
    T2=multiprocessing.Process(target=sumodd,args=(900000000,),)

    T1.start()
    T2.start()
    
    T1.join()
    T2.join()

    end_time=time.time()

    print("Rime Required execution is ",end_time - start_time)

    print("End of Main")

if __name__ == "__main__":
    main() 
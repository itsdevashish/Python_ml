import threading             
import time

def sumeven(no):
    sum=0
    for i in range(2,no+1,2):
        sum=sum+i
    print(sum)

def sumodd(no):
    sum=0
    for i in range(1,no+1,2):
        sum=sum+i
    print(sum)


def main():
    print("Demonstratation od parallel execuation")
    start_time=time.time()

    T1=threading.Thread(target=sumeven,args=(900000000,))
    T2=threading.Thread(target=sumodd,args=(900000000,),)

    T1.start()
    T2.start()
    
    T1.join()
    T2.join()

    end_time=time.time()

    print("Rime Required execution is ",end_time - start_time)

    print("End of Main")

if __name__ == "__main__":
    main() 
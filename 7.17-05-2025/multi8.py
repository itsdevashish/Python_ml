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
    print("Demonstratation od serial execuation")


    start_time=time.time()
    sumeven(900000000)
    sumodd(900000000)

    end_time=time.time()

    print("Rime Required execution is ",end_time - start_time)
    print("End of main")

if __name__ == "__main__":
    main() 
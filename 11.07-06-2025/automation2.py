import schedule
import time
import datetime

def myschedule():
    print("Inside My schedule function at",datetime.datetime.now())

def main():
    print("Inside Automation Script")
    print("current time is :",datetime.datetime.now())
    
    schedule.every(20).seconds.do(myschedule)

    print("End of automation script")

if __name__ == "__main__":
    main()
import schedule
import time
import datetime

def myschedule():
    print("Inside My schedule function at",datetime.datetime.now())

def myschedulex():
    print("Inside My schedulex function at",datetime.datetime.now())

def main():
    print("Inside Automation Script")
    print("current time is :",datetime.datetime.now())
    
    #schedule.every(20).minute.do(myschedule)
       
    schedule.every(1).minute.do(myschedulex)

    #schedule.every(1).hour.do(myschedulex)

    print("Application is in waiting state")

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()
import psutil

def processdisplay():
    border= "*"*35
    print(border)
    print("Information of currently runnning processes")
    print(border)

    for proc in psutil.process_iter():
        info=proc.as_dict(attrs=['pid','name','username'])
        info['vms']=proc.memory_info().vms/(1024*1024)
        print(info)


def main():
    processdisplay()
    

if __name__ =="__main__":
    main()
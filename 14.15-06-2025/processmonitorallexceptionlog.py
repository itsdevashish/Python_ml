import psutil


def processscan():
    listprocess=[]
    for proc in psutil.process_iter():
        try:
            info=proc.as_dict(attrs=['pid','name','username'])
            info['vms']=proc.memory_info().vms/(1024*1024)
            listprocess.append(info)
        except (psutil.NoSuchProcess,psutil.AccessDenied,psutil.ZombieProcess):
            pass
    return listprocess

def main():
    arr=processscan()
    print(arr)

    for value in arr:
        print (value)
    

if __name__ =="__main__":
    main()
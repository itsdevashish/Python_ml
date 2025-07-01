import psutil, os, time

def CreateLog(FolderName):
    if not os.path.exists(FolderName):
        os.mkdir(FolderName)
        
    timestap = time.ctime()
    timestap = timestap.replace(" ","")
    timestap = timestap.replace(":","_")
    timestap = timestap.replace("/","_")
    
    FileName = os.path.join(FolderName, "Marvellous%s.log" %(timestap))
    
    fobj =open(FileName, "w")
    
    Border = "-"*80
    fobj.write(Border)
    fobj.write("\n\t\tMarvellous Infosystems Process Log\n")
    fobj.write("\n\t\tLog file is created at : "+time.ctime()+"\n")
    fobj.write(Border)

def ProcessScan():
    listprocess = []
    
    for proc in psutil.process_iter():
        try:
            info = proc.as_dict(attrs=['pid', 'name', 'username'])
            info['vms'] = proc.memory_info().vms / (1024 * 1024)
            print(info)
            listprocess.append(info)
        except (psutil.NoSuchProcess,psutil.AccessDenied,psutil.ZombieProcess):
            pass
        
    return listprocess

def main():
    CreateLog("MarvellousProcess")
    
if __name__ == "__main__":
    main()
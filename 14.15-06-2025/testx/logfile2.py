import sys
import time

def main():
    timestamp=time.ctime()
    
    filename="Marvellouslog_%s.log"%(timestamp)
    filename=filename.replace(" ","_")
    filename=filename.replace(":","_")

    print(filename)
    fobj=open(filename,"w")


    border= "-"*54
    fobj.write(border+"\n")
    fobj.write("This a log file of marvellous automation script\n")
    fobj.write(border+"\n")


    fobj.write("\n\n\n\n\n\n\n\n\n\n\n\n")
    fobj.write(border+"\n")
    fobj.write("This is a created at \n"+timestamp+"\n")
    fobj.write(border+"\n")



if __name__ =="__main__":
    main()
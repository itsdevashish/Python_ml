
def add(no):
    sum=0
    while(no>=1):
        sum=sum+no
        no=no-1
    return sum

def main():
    ret=add(4)
    print(ret)

 
if __name__=="__main__":
    main()

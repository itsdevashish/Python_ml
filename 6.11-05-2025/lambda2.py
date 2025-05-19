def chkeven(no):
    if (no%2==0):
        return True
    else:
        return False

ret=chkeven(10)

if ret==True:
    print("Number is even")

else:
    print("Number is odd")
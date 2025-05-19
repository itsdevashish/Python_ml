
def power(x,y):
    result=1
    for i in range(y):
        result= result*x
    return result

ret=power(10,7)
print("Result is ",ret)
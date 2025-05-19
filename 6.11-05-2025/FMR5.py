
def increase(a):
    return a+1

def demo(task,value):
    result=[]
    for no in value:
       ret=task(no)
       result.append(ret)

    return result

data=[13,17,10,14,11]

rdata= list(demo(increase,data))

print(rdata)
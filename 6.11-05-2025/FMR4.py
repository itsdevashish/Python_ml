
def increase(a):
    return a+1

def demo(task,value):
    for no in value:
        print(task(no))
        


data=[13,17,10,14,11]

demo(increase,data)
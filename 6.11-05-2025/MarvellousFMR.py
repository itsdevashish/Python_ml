def filterX(task,values):
    result=[]
    for no in values:
        ret= task (no)
        if ret==True:
            result.append(no)
    return result

def mapX(task,values):
    result=[]
    for no in values:
        ret= task(no)
        result.append(ret)
    return result

def reduceX(task,values):
    result=0
    for no in values:
        result=task(result,no)
    return result
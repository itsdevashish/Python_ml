from functools import reduce

chkeven = lambda no:(no%2==0)

increase=lambda no : no+1

sum= lambda a,b :a+b


Data=[7,10,15,12,4,6,9,8,12,16]
print("Inpur Data :",Data)

FData= list(filter(chkeven,Data))
print("Filter Output :",FData)

MData=list(map(increase,FData))
print("Map Output :",MData)

RData=reduce(sum,MData)
print("Reduced Outpu :",RData)
#Tuple 
#syntax :()
#heterogenius
#ordered
#indexed
#data immutable
#tuple immutable
#duplicate allowed

data =(10,"hello",90.67,True)
print("Data type is : ",type(data))
print("Length is :",len(data))   
print(data) 


print(data[0])
print(data[1])

#data[0]=11

print("Data Using Loop :")
for value in (data):
    print(value)

print("Data Using Loop :")
for i in data:
    print (i)


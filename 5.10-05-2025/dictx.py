data={
"Name": "Let Us C", 
"Auther" : "Yashwant kanetkar",
"Price":340, 
"Publication" : "BPB Publication"
}

print("********--------------------***********")
print("loop to diplay keys")
for x in data:
    print (x)

print("********--------------------***********")

print("Loop to displays values")

for x in data.values():
    print(x)


print("********--------------------***********")
print("Loop to display key and value")
for x,y in data.items():
    print(x,y)



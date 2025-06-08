#Method oveloading not allowed 
class demo:
    
    def addition(a,b):
        return a+b
    
    def addition(a,b,c):
        return a+b+c
    

obj=demo()

print(obj.addition(10,11))

print(obj.addition(10,11),21)
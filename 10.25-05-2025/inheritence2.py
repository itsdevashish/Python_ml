class circle:
    PI=3.14
    def __init__(self,a):
        print("Inside Circle constructor")
        self.radius=a

    def calculatearea(self):
        answer=0.0
        answer =circle.PI*self.radius*self.radius
        return answer
    
class circlex(circle):
    def __init__(self,b):
        print("Inside Circle X constructor")
        super().__init__(b)

    def calculatecircumference(self):
        ans=0.0
        ans=2*circle.PI* self.radius
        return ans

    
def main():
    obj=circlex(10.5)

    ret=obj.calculatearea()
    print("Area of circle is :",ret)

    ret=obj.calculatecircumference()
    print("Circumference of circle is :",ret)

if __name__ == "__main__":
    main()
 
def circlearea(rad,PI=3.14):
    area=PI*rad*rad
    return area
 
 
def main():
    print("Enter Radius of circle")
    Radius=float(input())

    area=circlearea(Radius,7.12)
    print("The Radius Of circle is :",area)


if __name__ == "__main__":
    main()
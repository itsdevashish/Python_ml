PI=3.14
 
def circlearea(rad):
    area=PI*rad*rad
    return area
 
 
def main():
    print("Enter Radius od circle")
    Radius=float(input())

    area=circlearea(Radius)
    print("The Radius Of circle is",area)


if __name__ == "__main__":
    main()
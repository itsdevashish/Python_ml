#variable Argument
def display(*a):
    print(type(a))
    print("Inside Display",a)


def main():
    display(11,21,51,101)
    display(11,21,51,101,111)
    display(11,21,51)
    display(11)
    display()


if __name__ == "__main__":
    main()
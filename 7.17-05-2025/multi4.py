import threading              # new create->runnable->run->waiting->dead

def display():
    print("Inside Display")


def main():
    print("Inside Main")
    T1=threading.Thread(target=display)
    T1.start()


if __name__ == "__main__":
    main() 
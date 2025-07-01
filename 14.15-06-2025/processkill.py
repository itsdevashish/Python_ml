import psutil

def killprocess(name):
    for proc in psutil.process_iter(['name']):
        if proc.info['name']==name:
            print("Killing the process :",name)
            proc.kill()

def main():
    killprocess("Google Chrome")

if __name__ == "__main__":
    main()
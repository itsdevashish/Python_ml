import os

def main():
    for foldername ,subfolernames , filenames in os.walk("marvellous"):
        print("folder name is :"+foldername)
    
        for subf in subfolernames:
            print("subfolder name is :"+subf)
    
        for fname in filenames:
            print("file name is :"+fname)


if __name__ == "__main__":
    main()
#Automate git init process while making directory
import os
import sys

path = "/mnt/c/Users/frede/Documents/GitHub/"

def init():
    directoryName = str(sys.argv[1])
    try:
        os.makedirs(path + directoryName)
    except FileExistsError:
        print("This folder already exits")
    print("Directory {Directory} was created".format(Directory = directoryName))


if __name__ == "__main__":
    init()
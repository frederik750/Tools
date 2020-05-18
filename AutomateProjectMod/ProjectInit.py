#Automate git init process while making directory
import os
import sys
import datetime
import github
from Credentials import password

path = "/mnt/c/Users/frede/Documents/GitHub/"

def init():
    directoryName = str(sys.argv[1])
    try:
        os.makedirs(path + directoryName)
    except FileExistsError:
        print("This folder already exits")
    print("Directory {Directory} was created at {path} {time}".format(Directory = directoryName, path = path, time = str(datetime.datetime.now())))

if __name__ == "__main__":
    init()
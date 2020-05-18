import os
import sys
import datetime

path = "/mnt/c/Users/frede/Documents/GitHub/"

def Remove():
    directoryName = str(sys.argv[1])
    try:
        os.removedirs(path + directoryName)
    except FileNotFoundError:
        print("This folder does not exits")
    print("Directory {Directory} at {path} was deleted {time}".format(Directory = directoryName, path = path, time = str(datetime.datetime.now())))

if __name__ == "__main__":
    Remove()
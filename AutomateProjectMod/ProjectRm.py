import os
import sys
import datetime
from github import Github
from Credentials import token

path = "/mnt/c/Users/frede/Documents/GitHub/"

def Remove():
    directoryName = str(sys.argv[1])
    try:
        os.removedirs(path + directoryName)
        g = Github(token)
        g.get_repo(directoryName).delete()
        print("Directory {Directory} at {path} was deleted {time}".format(Directory = directoryName, path = path, time = str(datetime.datetime.now())))
    except FileNotFoundError:
        print("This folder does not exits")

if __name__ == "__main__":
    Remove()
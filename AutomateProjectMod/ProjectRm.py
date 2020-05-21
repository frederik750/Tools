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
        repo = g.get_repo("frederik750/" + directoryName)
        repo.delete()
        print("Directory {Directory} at {path} was deleted {time}".format(Directory = directoryName, path = path, time = str(datetime.datetime.now())))
    except FileNotFoundError:
        print("This folder does not exits")

if __name__ == "__main__":
    Remove()
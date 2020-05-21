import shutil
import sys
import datetime
from github import Github
from Credentials import token

path = "/mnt/c/Users/frede/Documents/GitHub/"

def Remove():
    directoryName = str(sys.argv[1])
    try:
        g = Github(token)
        repo = g.get_repo("frederik750/" + directoryName)
        repo.delete()
        print("Repository {Directory} was deleted from Github at {time}".format(Directory = directoryName, time = str(datetime.datetime.now())))
        shutil.rmtree(path + directoryName)
        print("Folder {Directory} at {path} was deleted {time}".format(Directory = directoryName, path = path, time = str(datetime.datetime.now())))

    except FileNotFoundError:
        print("This folder does not exits")

if __name__ == "__main__":
    Remove()
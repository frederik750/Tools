#Automate git init process while making directory
import os
import sys
import datetime
from Credentials import token
from github import Github
from git import Repo

path = "/mnt/c/Users/frede/Documents/GitHub/"

def init():
    directoryName = str(sys.argv[1])
    git_repo = "https://github.com/frederik750/" + directoryName + ".git"
    try:
        os.makedirs(path + directoryName)
        g = Github(token)
        user = g.get_user()
        user.create_repo(directoryName, auto_init=True)
        Repo.clone_from(git_repo, path + directoryName)
        print("Directory {Directory} was created at {path} {time}".format(Directory = directoryName, path = path, time = str(datetime.datetime.now())))
    except FileExistsError:
        print("This folder already exits")

if __name__ == "__main__":
    init()
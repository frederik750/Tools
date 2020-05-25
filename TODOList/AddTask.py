import sys

def AddTask():
    file_path = "/mnt/c/Users/frede/Documents/GitHub/Tools/TODOList/TODO.txt"
    try:
        f = open(file_path, "a")
        for i in range(1, len(sys.argv)):
            f.write(str(sys.argv[i]) + " ")
        f.write("\n")
        f.close()
    except IOError as e:
        print(e)

if(__name__ == "__main__"):
    AddTask()
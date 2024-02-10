import sys

def openfile():

    filename = sys.argv[1]
    data = sys.argv[2]
    file = open(filename,"a")
    file.write(data)
    file.close()


openfile()

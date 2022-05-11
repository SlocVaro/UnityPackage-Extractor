import tarfile
import os

def getFolder(file_name):
    folder = file_name.split(".")
    del folder[-1]
    return ".".join(folder)

def extract(file_name):
    folder = "_{}".format(getFolder(file_name))
    os.mkdir(folder)
    tar = tarfile.open(file_name)
    print('Extracting "{}"'.format(file_name))
    tar.extractall(folder)
    tar.close()
#!/usr/bin/python
import sys
import os
import datetime
def gettime(fileordir):
    return os.path.getctime(fileordir)

def isotime(timestamp):
    return datetime.datetime.utcfromtimestamp(timestamp).strftime('%Y-%m-%dT%H:%M:%SZ')

for root, dirs, files in os.walk(".", topdown=False):
    for name in files:
        try:
            if int(gettime(root)) < int(gettime(os.path.join(root, name))):
                print(isotime(gettime(root)), root, isotime(gettime(os.path.join(root, name))), os.path.join(root, name))
        except OSError:
            print("OSError issues with: " + os.path.join(root, name))
    for name in dirs:
        try:
            if int(gettime(root)) < int(gettime(os.path.join(root, name))):
                print(isotime(gettime(root)), root, isotime(gettime(os.path.join(root, name))), os.path.join(root, name))
        except OSError:
            print("OSError issues with: " + os.path.join(root, name))

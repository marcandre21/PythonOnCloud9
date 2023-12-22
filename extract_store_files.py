#!/usr/bin/python

import os, sys

# Open a file
path = path = './'
directory = os.listdir(path)

#Print all the files and directories
for file in directory:
      print(file)
 
cwd = os.getcwd()
print("MPL")

for name in os.listdir(cwd):
   
    for file_size in range(os.path.getsize(cwd)):
       
        file_attr = {
    "name": name,
    "size": os.path.getsize(name)
}

    print(file_attr)

#List out dicts

l = os.listdir (path)
print(l)

for root, dirs, file in os.walk(path):
    print(file)

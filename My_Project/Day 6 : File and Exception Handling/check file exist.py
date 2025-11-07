#os.path.exists()

import os
from pathlib import Path

filename= "practice.txt"
if not os.path.exists(filename):  # we can pass the file path also to check the existence of file
    print("File does not exist")
else:
    print("File exists")

#Pathlib.Path.exists()
filename= Path("practice.txt")
if filename.exists():
    print("File exists")
else:
    print("File does not exist")

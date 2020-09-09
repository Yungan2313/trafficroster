import shutil
import os

shutil.copyfile("p.txt","p1.txt")
a = int(input("5"))
if a == 5:
    os.remove("p1.txt")
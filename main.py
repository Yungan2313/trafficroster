import re
import shutil
import tkinter as tk
import random
#--------------------------------------------tkinter
# main = tk.Tk()

# main.geometry("800x600")

# main.title("trafficroster")

# main.mainloop()

#--------------------------------------------檔案讀取
shutil.copyfile("p.txt","p1.txt")
ptxt = open("p1.txt","r",encoding="utf-8")
line = len(ptxt.readlines())
per = [[0] *10 for i in range(line)]
ptxt = open("p1.txt","r",encoding="utf-8")
for i in range(line):
    f = ptxt.readline()
    per[i] = list(f.split())
#--------------------------------------------判斷
ros = [[0] *15 for i in range(10)]
#早上正打
for j in range(0,5):
    i = 10
    p1 = 1234
    while i!=12:
        p = random.randrange(0,line)
        if p == p1:
            continue
        if per[p][5] == "1":
            day = []
            d = per[p][1]
            day = list(d.split(","))    
            per[p][6] = int(per[p][6])
            if day[j] != "0" and per[p][6]>0:
                ros[j][i] = per[p][0]
                per[p][6]-=1
                i = i+1
                p1 = p
#
            

            

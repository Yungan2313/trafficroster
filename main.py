import re
import shutil
import tkinter as tk
import random
import os
#--------------------------------------------tkinter
# main = tk.Tk()

# main.geometry("800x600")

# main.title("trafficroster")

# #frame1
# two = tk.Label(main,text = "二線")
# lwol = tk.Label(main,text = "魯班")
# lwor = tk.Label(main,text = "魯班")
# noguanf = tk.Label(main,text = "北管")
# noguanb = tk.Label(main,text = "北管")
# twopunl = tk.Label(main,text = "二打")
# twopunt = tk.Label(main,text = "二打")
# rigpunk = tk.Label(main,text = "正打")
# rigpunb = tk.Label(main,text = "正打")
# punthr = tk.Label(main,text = "打三")
# twodun = tk.Label(main,text = "二燈")
# bigdun = tk.Label(main,text = "大燈")

# main.mainloop()

#--------------------------------------------檔案讀取
ptxt = open("p.txt","r",encoding="utf-8")
line = len(ptxt.readlines())
per = [[0] *10 for i in range(line)]
ptxt = open("p.txt","r",encoding="utf-8")
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
            per[p][3] = int(per[p][3])
            if day[j] != "0" and per[p][6]>0:
                ros[j][i] = per[p][0]
                per[p][6]-=1
                per[p][3]-=1
                day[0] = "0"
                per[p][1] = "{0},{1},{2},{3},{4}".format(day[0],day[1],day[2],day[3],day[4])
                print(per[p][1])
                i = i+1
                p1 = p
#下午正打 
for j in range(5,10):
    i = 10
    p1 = 1234
    while i!=12:
        p = random.randrange(0,line)
        if p == p1:
            continue
        if per[p][5] == "1":
            day = []
            d = per[p][2]
            day = list(d.split(","))   
            per[p][6] = int(per[p][6])
            per[p][3] = int(per[p][3])
            if day[j-5] != "0" and per[p][6]>0:
                ros[j][i] = per[p][0]
                per[p][6]-=1
                per[p][3]-=1
                i = i+1
                p1 = p
#大燈
for j in range(0,5):
    i = 14
    while i!=15:
        p = random.randrange(0,line)
        if per[p][9] == "1":
            day = []
            d = per[p][1]
            day = list(d.split(","))    
            per[p][9] = int(per[p][9])
            per[p][3] = int(per[p][3])
            if day[j] != "0" and per[p][9]>0:
                ros[j][i] = per[p][0]
                per[p][9]-=1
                per[p][3]-=1
                i = i+1
#下午大燈
for j in range(5,10):
    i = 14
    while i!=15:
        p = random.randrange(0,line)
        if per[p][9] == "1":
            day = []
            d = per[p][2]
            day = list(d.split(","))    
            per[p][9] = int(per[p][9])
            per[p][3] = int(per[p][3])
            if day[j-5] != "0" and per[p][9]>0:
                ros[j][i] = per[p][0]
                per[p][9]-=1
                per[p][3]-=1
                i = i+1
#上午二燈
for j in range(0,5):
    i = 13
    while i!=14:
        p = random.randrange(0,line)
        if per[p][8] == "1":
            day = []
            d = per[p][1]
            day = list(d.split(","))    
            per[p][8] = int(per[p][8])
            per[p][3] = int(per[p][3])
            if day[j] != "0" and per[p][8]>0:
                ros[j][i] = per[p][0]
                per[p][8]-=1
                per[p][3]-=1
                i = i+1
#下午二燈
for j in range(5,10):
    i = 13
    while i!=14:
        p = random.randrange(0,line)
        if per[p][8] == "1":
            day = []
            d = per[p][2]
            day = list(d.split(","))    
            per[p][8] = int(per[p][8])
            per[p][3] = int(per[p][3])
            if day[j-5] != "0" and per[p][8]>0:
                ros[j][i] = per[p][0]
                per[p][8]-=1
                per[p][3]-=1
                i = i+1
#上午打三
for j in range(0,5):
    i = 12
    while i!=13:
        p = random.randrange(0,line)
        if per[p][7] == "1":
            day = []
            d = per[p][1]
            day = list(d.split(","))    
            per[p][7] = int(per[p][7])
            per[p][3] = int(per[p][3])
            if day[j] != "0" and per[p][7]>0:
                ros[j][i] = per[p][0]
                per[p][3]-=1
                i = i+1
#下午打三
for j in range(5,10):
    i = 12
    while i!=13:
        p = random.randrange(0,line)
        if per[p][7] == "1":
            day = []
            d = per[p][2]
            day = list(d.split(","))    
            per[p][7] = int(per[p][7])
            per[p][3] = int(per[p][3])
            if day[j-5] != "0" and per[p][7]>0:
                ros[j][i] = per[p][0]
                per[p][3]-=1
                i = i+1
#上午北管
for j in range(0,5):
    i = 6
    p1 = 1234
    while i!=8:
        p = random.randrange(0,line)
        if p == p1:
            continue
        if per[p][7] == "1":
            day = []
            d = per[p][1]
            day = list(d.split(","))    
            per[p][7] = int(per[p][7])
            per[p][3] = int(per[p][3])
            if day[j] != "0" and per[p][7]>0:
                ros[j][i] = per[p][0]
                per[p][3]-=1
                i = i+1
                p1 = p
#下午北管
for j in range(5,10):
    i = 6
    p1 = 1234
    while i!=8:
        p = random.randrange(0,line)
        if p == p1:
            continue
        if per[p][7] == "1":
            day = []
            d = per[p][2]
            day = list(d.split(","))    
            per[p][7] = int(per[p][7])
            per[p][3] = int(per[p][3])
            if day[j-5] != "0" and per[p][7]>0:
                ros[j][i] = per[p][0]
                per[p][3]-=1
                i = i+1
                p1 = p
                print(ros[j][i-1])
#早上二打
for j in range(0,5):
    i = 8
    p1 = 1234
    while i!=10:
        p = random.randrange(0,line)
        if p == p1:
            continue
        if per[p][4] != "1":
            day = []
            d = per[p][1]
            day = list(d.split(","))    
            per[p][4] = int(per[p][4])
            per[p][3] = int(per[p][3])
            if day[j] != "0" and per[p][4]>0:
                ros[j][i] = per[p][0]
                per[p][3]-=1
                i = i+1
                p1 = p
#下午二打
for j in range(5,10):
    i = 8
    p1 = 1234
    while i!=10:
        p = random.randrange(0,line)
        if p == p1:
            continue
        if per[p][4] != "1":
            day = []
            d = per[p][2]
            day = list(d.split(","))    
            per[p][4] = int(per[p][4])
            per[p][3] = int(per[p][3])
            if day[j-5] != "0" and per[p][4]>0:
                ros[j][i] = per[p][0]
                per[p][3]-=1
                i = i+1
                p1 = p
#上午大檔
for j in range(0,5):
    i = 4
    p1 = 1234
    while i!=6:
        p = random.randrange(0,line)
        if p == p1:
            continue
        if per[p][4] != "1":
            day = []
            d = per[p][1]
            day = list(d.split(","))    
            per[p][4] = int(per[p][4])
            per[p][3] = int(per[p][3])
            if day[j] != "0" and per[p][4]>0:
                ros[j][i] = per[p][0]
                per[p][3]-=1
                i = i+1
                p1 = p
#下午大檔
for j in range(5,10):
    i = 4
    p1 = 1234
    while i!=6:
        p = random.randrange(0,line)
        if p == p1:
            continue
        if per[p][4] != "1":
            day = []
            d = per[p][2]
            day = list(d.split(","))    
            per[p][4] = int(per[p][4])
            per[p][3] = int(per[p][3])
            if day[j-5] != "0" and per[p][4]>0:
                ros[j][i] = per[p][0]
                per[p][3]-=1
                i = i+1
                p1 = p
#上午魯班
for j in range(0,5):
    i = 2
    p1 = 1234
    while i!=4:
        p = random.randrange(0,line)
        if p == p1:
            continue
        if per[p][4] != "1":
            day = []
            d = per[p][1]
            day = list(d.split(","))    
            per[p][4] = int(per[p][4])
            per[p][3] = int(per[p][3])
            if day[j] != "0" and per[p][4]>0:
                ros[j][i] = per[p][0]
                per[p][3]-=1
                i = i+1
                p1 = p
#下午魯班
for j in range(5,10):
    i = 2
    p1 = 1234
    while i!=4:
        p = random.randrange(0,line)
        if p == p1:
            continue
        if per[p][4] != "1":
            day = []
            d = per[p][2]
            day = list(d.split(","))    
            per[p][4] = int(per[p][4])
            per[p][3] = int(per[p][3])
            if day[j-5] != "0" and per[p][4]>0:
                ros[j][i] = per[p][0]
                per[p][3]-=1
                i = i+1
                p1 = p
#二線
for j in range(0,5):
    i = 1
    p = random.randrange(0,line)
    if per[p][4] != "1":
        day = []
        d = per[p][1]
        day = list(d.split(","))    
        per[p][4] = int(per[p][4])
        per[p][3] = int(per[p][3])
        if day[j] != "0" and per[p][4]>0:
            ros[j][i] = per[p][0]
            per[p][3]-=1
            i = i+1

import re
import shutil
import tkinter as tk
import random
import os
from  tkinter import ttk
#--------------------------------------------tkinter
win=tk.Tk()
tree=ttk.Treeview(win)#表格
tree["columns"]=("二線","魯班","大檔","北管","二打","正打","打三","二燈","大燈")
#表示列,不显示
tree.column("二線",width=100)
tree.column("魯班",width=100)
tree.column("大檔",width=100)
tree.column("北管",width=100)
tree.column("二打",width=100)
tree.column("正打",width=100)
tree.column("打三",width=50)
tree.column("二燈",width=50)
tree.column("大燈",width=50)

tree.heading("二線",text="二線")
tree.heading("魯班",text="魯班")  #显示表头
tree.heading("大檔",text="大檔")
tree.heading("北管",text="北管")
tree.heading("二打",text="二打")
tree.heading("正打",text="正打")
tree.heading("打三",text="打三")
tree.heading("二燈",text="二燈")
tree.heading("大燈",text="大燈")
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
# #早上正打
# for j in range(0,5):
#     i = 9
#     p1 = 1234
#     while i!=11:
#         p = random.randrange(0,line)
#         if p == p1:
#             continue
#         if per[p][5] == "1":
#             day = []
#             d = per[p][1]
#             day = list(d.split(","))    
#             per[p][6] = int(per[p][6])
#             per[p][3] = int(per[p][3])
#             if day[j] != "0" and per[p][6]>0:
#                 ros[j][i] = per[p][0]
#                 per[p][6]-=1
#                 per[p][3]-=1
#                 day[j] = "0"
#                 per[p][1] = "{0},{1},{2},{3},{4}".format(day[0],day[1],day[2],day[3],day[4])
#                 i = i+1
#                 p1 = p
# #下午正打 
# for j in range(5,10):
#     i = 9
#     p1 = 1234
#     while i!=11:
#         p = random.randrange(0,line)
#         if p == p1:
#             continue
#         if per[p][5] == "1":
#             day = []
#             d = per[p][2]
#             day = list(d.split(","))   
#             per[p][6] = int(per[p][6])
#             per[p][3] = int(per[p][3])
#             if day[j-5] != "0" and per[p][6]>0:
#                 ros[j][i] = per[p][0]
#                 per[p][6]-=1
#                 per[p][3]-=1
#                 day[j-5] = "0"
#                 per[p][2] = "{0},{1},{2},{3},{4}".format(day[0],day[1],day[2],day[3],day[4])
#                 i = i+1
#                 p1 = p
# #上午大燈
# for j in range(0,5):
#     i = 13
#     while i!=14:
#         p = random.randrange(0,line)
#         if per[p][9] == "1":
#             day = []
#             d = per[p][1]
#             day = list(d.split(","))    
#             per[p][9] = int(per[p][9])
#             per[p][3] = int(per[p][3])
#             if day[j] != "0" and per[p][9]>0:
#                 ros[j][i] = per[p][0]
#                 per[p][9]-=1
#                 per[p][3]-=1
#                 day[j] = "0"
#                 per[p][1] = "{0},{1},{2},{3},{4}".format(day[0],day[1],day[2],day[3],day[4])
#                 i = i+1
# #下午大燈
# for j in range(5,10):
#     i = 13
#     while i!=14:
#         p = random.randrange(0,line)
#         if per[p][9] == "1":
#             day = []
#             d = per[p][2]
#             day = list(d.split(","))    
#             per[p][9] = int(per[p][9])
#             per[p][3] = int(per[p][3])
#             if day[j-5] != "0" and per[p][9]>0:
#                 ros[j][i] = per[p][0]
#                 per[p][9]-=1
#                 per[p][3]-=1
#                 day[j-5] = "0"
#                 per[p][2] = "{0},{1},{2},{3},{4}".format(day[0],day[1],day[2],day[3],day[4])
#                 i = i+1
# #上午二燈
# for j in range(0,5):
#     i = 12
#     while i!=13:
#         p = random.randrange(0,line)
#         if per[p][8] == "1":
#             day = []
#             d = per[p][1]
#             day = list(d.split(","))    
#             per[p][8] = int(per[p][8])
#             per[p][3] = int(per[p][3])
#             if day[j] != "0" and per[p][8]>0:
#                 ros[j][i] = per[p][0]
#                 per[p][8]-=1
#                 per[p][3]-=1
#                 day[j] = "0"
#                 per[p][1] = "{0},{1},{2},{3},{4}".format(day[0],day[1],day[2],day[3],day[4])
#                 i = i+1
# #下午二燈
# for j in range(5,10):
#     i = 12
#     while i!=13:
#         p = random.randrange(0,line)
#         if per[p][8] == "1":
#             day = []
#             d = per[p][2]
#             day = list(d.split(","))    
#             per[p][8] = int(per[p][8])
#             per[p][3] = int(per[p][3])
#             if day[j-5] != "0" and per[p][8]>0:
#                 ros[j][i] = per[p][0]
#                 per[p][8]-=1
#                 per[p][3]-=1
#                 day[j-5] = "0"
#                 per[p][2] = "{0},{1},{2},{3},{4}".format(day[0],day[1],day[2],day[3],day[4])
#                 i = i+1
# #上午打三
# for j in range(0,5):
#     i = 11
#     while i!=12:
#         p = random.randrange(0,line)
#         if per[p][7] == "1":
#             day = []
#             d = per[p][1]
#             day = list(d.split(","))    
#             per[p][7] = int(per[p][7])
#             per[p][3] = int(per[p][3])
#             if day[j] != "0" and per[p][7]>0:
#                 ros[j][i] = per[p][0]
#                 per[p][3]-=1
#                 day[j] = "0"
#                 per[p][1] = "{0},{1},{2},{3},{4}".format(day[0],day[1],day[2],day[3],day[4])
#                 i = i+1
# #下午打三
# for j in range(5,10):
#     i = 11
#     while i!=12:
#         p = random.randrange(0,line)
#         if per[p][7] == "1":
#             day = []
#             d = per[p][2]
#             day = list(d.split(","))    
#             per[p][7] = int(per[p][7])
#             per[p][3] = int(per[p][3])
#             if day[j-5] != "0" and per[p][7]>0:
#                 ros[j][i] = per[p][0]
#                 per[p][3]-=1
#                 day[j-5] = "0"
#                 per[p][2] = "{0},{1},{2},{3},{4}".format(day[0],day[1],day[2],day[3],day[4])
#                 i = i+1
# #上午北管
# for j in range(0,5):
#     i = 5
#     p1 = 1234
#     while i!=7:
#         p = random.randrange(0,line)
#         if p == p1:
#             continue
#         if per[p][7] == "1":
#             day = []
#             d = per[p][1]
#             day = list(d.split(","))    
#             per[p][7] = int(per[p][7])
#             per[p][3] = int(per[p][3])
#             if day[j] != "0" and per[p][7]>0:
#                 ros[j][i] = per[p][0]
#                 per[p][3]-=1
#                 day[j] = "0"
#                 per[p][1] = "{0},{1},{2},{3},{4}".format(day[0],day[1],day[2],day[3],day[4])
#                 i = i+1
#                 p1 = p
# #下午北管
# for j in range(5,10):
#     i = 5
#     p1 = 1234
#     while i!=7:
#         p = random.randrange(0,line)
#         if p == p1:
#             continue
#         if per[p][7] == "1":
#             day = []
#             d = per[p][2]
#             day = list(d.split(","))    
#             per[p][7] = int(per[p][7])
#             per[p][3] = int(per[p][3])
#             if day[j-5] != "0" and per[p][7]>0:
#                 ros[j][i] = per[p][0]
#                 per[p][3]-=1
#                 day[j-5] = "0"
#                 per[p][2] = "{0},{1},{2},{3},{4}".format(day[0],day[1],day[2],day[3],day[4])
#                 i = i+1
#                 p1 = p
# #早上二打
# for j in range(0,5):
#     i = 7
#     p1 = 1234
#     while i!=9:
#         p = random.randrange(0,line)
#         if p == p1:
#             continue
#         if per[p][4] != "1":
#             day = []
#             d = per[p][1]
#             day = list(d.split(","))    
#             per[p][4] = int(per[p][4])
#             per[p][3] = int(per[p][3])
#             if day[j] != "0" and per[p][4]>0:
#                 ros[j][i] = per[p][0]
#                 per[p][3]-=1
#                 day[j] = "0"
#                 per[p][1] = "{0},{1},{2},{3},{4}".format(day[0],day[1],day[2],day[3],day[4])
#                 i = i+1
#                 p1 = p
# #下午二打
# for j in range(5,10):
#     i = 7
#     p1 = 1234
#     while i!=9:
#         p = random.randrange(0,line)
#         if p == p1:
#             continue
#         if per[p][4] != "1":
#             day = []
#             d = per[p][2]
#             day = list(d.split(","))    
#             per[p][4] = int(per[p][4])
#             per[p][3] = int(per[p][3])
#             if day[j-5] != "0" and per[p][4]>0:
#                 ros[j][i] = per[p][0]
#                 per[p][3]-=1
#                 day[j-5] = "0"
#                 per[p][2] = "{0},{1},{2},{3},{4}".format(day[0],day[1],day[2],day[3],day[4])
#                 i = i+1
#                 p1 = p
# #上午大檔
# for j in range(0,5):
#     i = 3
#     p1 = 1234
#     while i!=5:
#         p = random.randrange(0,line)
#         if p == p1:
#             continue
#         if per[p][4] != "1":
#             day = []
#             d = per[p][1]
#             day = list(d.split(","))    
#             per[p][4] = int(per[p][4])
#             per[p][3] = int(per[p][3])
#             if day[j] != "0" and per[p][4]>0:
#                 ros[j][i] = per[p][0]
#                 per[p][3]-=1
#                 day[j] = "0"
#                 per[p][1] = "{0},{1},{2},{3},{4}".format(day[0],day[1],day[2],day[3],day[4])
#                 i = i+1
#                 p1 = p
# #下午大檔
# for j in range(5,10):
#     i = 3
#     p1 = 1234
#     while i!=5:
#         p = random.randrange(0,line)
#         if p == p1:
#             continue
#         if per[p][4] != "1":
#             day = []
#             d = per[p][2]
#             day = list(d.split(","))    
#             per[p][4] = int(per[p][4])
#             per[p][3] = int(per[p][3])
#             if day[j-5] != "0" and per[p][4]>0:
#                 ros[j][i] = per[p][0]
#                 per[p][3]-=1
#                 day[j-5] = "0"
#                 per[p][2] = "{0},{1},{2},{3},{4}".format(day[0],day[1],day[2],day[3],day[4])
#                 i = i+1
#                 p1 = p
# #上午魯班
# for j in range(0,5):
#     i = 1
#     p1 = 1234
#     while i!=3:
#         p = random.randrange(0,line)
#         if p == p1:
#             continue
#         if per[p][4] != "1":
#             day = []
#             d = per[p][1]
#             day = list(d.split(","))    
#             per[p][4] = int(per[p][4])
#             per[p][3] = int(per[p][3])
#             if day[j] != "0" and per[p][4]>0:
#                 ros[j][i] = per[p][0]
#                 per[p][3]-=1
#                 day[j] = "0"
#                 per[p][1] = "{0},{1},{2},{3},{4}".format(day[0],day[1],day[2],day[3],day[4])
#                 i = i+1
#                 p1 = p
# #下午魯班
# for j in range(5,10):
#     i = 1
#     p1 = 1234
#     while i!=3:
#         p = random.randrange(0,line)
#         if p == p1:
#             continue
#         if per[p][4] != "1":
#             day = []
#             d = per[p][2]
#             day = list(d.split(","))    
#             per[p][4] = int(per[p][4])
#             per[p][3] = int(per[p][3])
#             if day[j-5] != "0" and per[p][4]>0:
#                 ros[j][i] = per[p][0]
#                 per[p][3]-=1
#                 day[j-5] = "0"
#                 per[p][2] = "{0},{1},{2},{3},{4}".format(day[0],day[1],day[2],day[3],day[4])
#                 i = i+1
#                 p1 = p
#二線
for j in range(0,5):
    i = 0
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
            day[j] = "0"
            per[p][1] = "{0},{1},{2},{3},{4}".format(day[0],day[1],day[2],day[3],day[4])
            i = i+1
#------------------------------------
tree.insert("",0,text="星期一上午" ,values=("{0}".format(ros[0][0]),"{0}  {1}".format(ros[0][1],ros[0][2]),"{0}  {1}".format(ros[0][3],ros[0][4]),"{0}  {1}".format(ros[0][5],ros[0][6]),"{0}  {1}".format(ros[0][7],ros[0][8]),"{0}  {1}".format(ros[0][9],ros[0][10]),"{0}".format(ros[0][11]),"{0}".format(ros[0][12]),"{0}".format(ros[0][13]))) #插入数据，
tree.insert("",1,text="星期一下午" ,values=("{0}".format(ros[5][0]),"{0}  {1}".format(ros[5][1],ros[5][2]),"{0}  {1}".format(ros[5][3],ros[5][4]),"{0}  {1}".format(ros[5][5],ros[5][6]),"{0}  {1}".format(ros[5][7],ros[5][8]),"{0}  {1}".format(ros[5][9],ros[5][10]),"{0}".format(ros[5][11]),"{0}".format(ros[5][12]),"{0}".format(ros[5][13])))
tree.insert("",2,text="星期二上午" ,values=("{0}".format(ros[1][0]),"{0}  {1}".format(ros[1][1],ros[1][2]),"{0}  {1}".format(ros[1][3],ros[1][4]),"{0}  {1}".format(ros[1][5],ros[1][6]),"{0}  {1}".format(ros[1][7],ros[1][8]),"{0}  {1}".format(ros[1][9],ros[1][10]),"{0}".format(ros[1][11]),"{0}".format(ros[1][12]),"{0}".format(ros[1][13])))
tree.insert("",3,text="星期二下午" ,values=("{0}".format(ros[6][0]),"{0}  {1}".format(ros[6][1],ros[6][2]),"{0}  {1}".format(ros[6][3],ros[6][4]),"{0}  {1}".format(ros[6][5],ros[6][6]),"{0}  {1}".format(ros[6][7],ros[6][8]),"{0}  {1}".format(ros[6][9],ros[6][10]),"{0}".format(ros[6][11]),"{0}".format(ros[6][12]),"{0}".format(ros[6][13])))
tree.insert("",4,text="星期三上午" ,values=("{0}".format(ros[2][0]),"{0}  {1}".format(ros[2][1],ros[2][2]),"{0}  {1}".format(ros[2][3],ros[2][4]),"{0}  {1}".format(ros[2][5],ros[2][6]),"{0}  {1}".format(ros[2][7],ros[2][8]),"{0}  {1}".format(ros[2][9],ros[2][10]),"{0}".format(ros[2][11]),"{0}".format(ros[2][12]),"{0}".format(ros[2][13])))
tree.insert("",5,text="星期三下午" ,values=("{0}".format(ros[7][0]),"{0}  {1}".format(ros[7][1],ros[7][2]),"{0}  {1}".format(ros[7][3],ros[7][4]),"{0}  {1}".format(ros[7][5],ros[7][6]),"{0}  {1}".format(ros[7][7],ros[7][8]),"{0}  {1}".format(ros[7][9],ros[7][10]),"{0}".format(ros[7][11]),"{0}".format(ros[7][12]),"{0}".format(ros[7][13])))
tree.insert("",6,text="星期四上午" ,values=("{0}".format(ros[3][0]),"{0}  {1}".format(ros[3][1],ros[3][2]),"{0}  {1}".format(ros[3][3],ros[3][4]),"{0}  {1}".format(ros[3][5],ros[3][6]),"{0}  {1}".format(ros[3][7],ros[3][8]),"{0}  {1}".format(ros[3][9],ros[3][10]),"{0}".format(ros[3][11]),"{0}".format(ros[3][12]),"{0}".format(ros[3][13])))
tree.insert("",7,text="星期四下午" ,values=("{0}".format(ros[8][0]),"{0}  {1}".format(ros[8][1],ros[8][2]),"{0}  {1}".format(ros[8][3],ros[8][4]),"{0}  {1}".format(ros[8][5],ros[8][6]),"{0}  {1}".format(ros[8][7],ros[8][8]),"{0}  {1}".format(ros[8][9],ros[8][10]),"{0}".format(ros[8][11]),"{0}".format(ros[8][12]),"{0}".format(ros[8][13])))
tree.insert("",8,text="星期五上午" ,values=("{0}".format(ros[4][0]),"{0}  {1}".format(ros[4][1],ros[4][2]),"{0}  {1}".format(ros[4][3],ros[4][4]),"{0}  {1}".format(ros[4][5],ros[4][6]),"{0}  {1}".format(ros[4][7],ros[4][8]),"{0}  {1}".format(ros[4][9],ros[4][10]),"{0}".format(ros[4][11]),"{0}".format(ros[4][12]),"{0}".format(ros[4][13])))
tree.insert("",9,text="星期五下午" ,values=("{0}".format(ros[9][0]),"{0}  {1}".format(ros[9][1],ros[9][2]),"{0}  {1}".format(ros[9][3],ros[9][4]),"{0}  {1}".format(ros[9][5],ros[9][6]),"{0}  {1}".format(ros[9][7],ros[9][8]),"{0}  {1}".format(ros[9][9],ros[9][10]),"{0}".format(ros[9][11]),"{0}".format(ros[9][12]),"{0}".format(ros[9][13])))
 
tree.pack()
win.mainloop()

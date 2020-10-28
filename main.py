import re
import shutil
import tkinter as tk
import random
import os
from  tkinter import ttk
from  tkinter import END
from functools import partial
#--------------------------------------------
def start():
    global line,ros
    
    #早上正打
    for j in range(0,5):
        i = 9
        p1 = 1234
        random.shuffle(layer)
        l = -1
        while i!=11:
            l += 1
            if l == line:
                break
            p = layer[l]
            if p == p1:
                continue
            per[p][5] = str(per[p][5])
            if per[p][5] == "1":
                if ros[j][i] !=0:
                    break
                day = []
                d = per[p][1]
                day = list(d.split(","))    
                per[p][6] = int(per[p][6])
                per[p][3] = int(per[p][3])
                if day[j] != "0" and per[p][6]>0:
                    ros[j][i] = per[p][0]
                    per[p][6]-=1
                    per[p][3]-=1
                    day[j] = "0"
                    per[p][1] = "{0},{1},{2},{3},{4}".format(day[0],day[1],day[2],day[3],day[4])
                    i = i+1
                    p1 = p
    #下午正打 
    for j in range(5,10):
        i = 9
        p1 = 1234
        random.shuffle(layer)
        l = -1
        while i!=11:
            l += 1
            if l == line:
                break
            p = layer[l]
            if p == p1:
                continue
            per[p][5] = str(per[p][5])
            if per[p][5] == "1":
                if ros[j][i] !=0:
                    break
                day = []
                d = per[p][2]
                day = list(d.split(","))   
                per[p][6] = int(per[p][6])
                per[p][3] = int(per[p][3])
                if day[j-5] != "0" and per[p][6]>0:
                    ros[j][i] = per[p][0]
                    per[p][6]-=1
                    per[p][3]-=1
                    day[j-5] = "0"
                    per[p][2] = "{0},{1},{2},{3},{4}".format(day[0],day[1],day[2],day[3],day[4])
                    i = i+1
                    p1 = p
    #上午大燈
    for j in range(0,5):
        i = 13
        random.shuffle(layer)
        l = -1
        while i!=14:
            l += 1
            if l == line:
                break
            p = layer[l]
            per[p][9] = str(per[p][9])
            if per[p][9] == "1":
                if ros[j][i] !=0:
                    break
                day = []
                d = per[p][1]
                day = list(d.split(","))    
                per[p][9] = int(per[p][9])
                per[p][3] = int(per[p][3])
                if day[j] != "0" and per[p][9]>0:
                    ros[j][i] = per[p][0]
                    per[p][9]-=1
                    per[p][3]-=1
                    day[j] = "0"
                    per[p][1] = "{0},{1},{2},{3},{4}".format(day[0],day[1],day[2],day[3],day[4])
                    i = i+1
    #下午大燈
    for j in range(5,10):
        i = 13
        random.shuffle(layer)
        l = -1
        while i!=14:
            l += 1
            if l == line:
                break
            p = layer[l]
            per[p][9] = str(per[p][9])
            if per[p][9] == "1":
                if ros[j][i] !=0:
                    break
                day = []
                d = per[p][2]
                day = list(d.split(","))    
                per[p][9] = int(per[p][9])
                per[p][3] = int(per[p][3])
                if day[j-5] != "0" and per[p][9]>0:
                    ros[j][i] = per[p][0]
                    per[p][9]-=1
                    per[p][3]-=1
                    day[j-5] = "0"
                    per[p][2] = "{0},{1},{2},{3},{4}".format(day[0],day[1],day[2],day[3],day[4])
                    i = i+1
    #上午二燈
    for j in range(0,5):
        i = 12
        random.shuffle(layer)
        l = -1
        while i!=13:
            l += 1
            if l == line:
                break
            p = layer[l]
            per[p][8] = str(per[p][8])
            if per[p][8] == "1":
                if ros[j][i] !=0:
                    break
                day = []
                d = per[p][1]
                day = list(d.split(","))    
                per[p][8] = int(per[p][8])
                per[p][3] = int(per[p][3])
                if day[j] != "0" and per[p][8]>0:
                    ros[j][i] = per[p][0]
                    per[p][8]-=1
                    per[p][3]-=1
                    day[j] = "0"
                    per[p][1] = "{0},{1},{2},{3},{4}".format(day[0],day[1],day[2],day[3],day[4])
                    i = i+1
    #下午二燈
    for j in range(5,10):
        i = 12
        random.shuffle(layer)
        l = -1
        while i!=13:
            l += 1
            if l == line:
                break
            p = layer[l]
            per[p][8] = str(per[p][8])
            if per[p][8] == "1":
                if ros[j][i] !=0:
                    break
                day = []
                d = per[p][2]
                day = list(d.split(","))    
                per[p][8] = int(per[p][8])
                per[p][3] = int(per[p][3])
                if day[j-5] != "0" and per[p][8]>0:
                    ros[j][i] = per[p][0]
                    per[p][8]-=1
                    per[p][3]-=1
                    day[j-5] = "0"
                    per[p][2] = "{0},{1},{2},{3},{4}".format(day[0],day[1],day[2],day[3],day[4])
                    i = i+1
    #上午打三
    for j in range(0,5):
        i = 11
        random.shuffle(layer)
        l = -1
        while i!=12:
            l += 1
            if l == line:
                break
            p = layer[l]
            per[p][7] = str(per[p][7])
            if per[p][7] == "1":
                if ros[j][i] !=0:
                    break
                day = []
                d = per[p][1]
                day = list(d.split(","))    
                per[p][7] = int(per[p][7])
                per[p][3] = int(per[p][3])
                if day[j] != "0":
                    ros[j][i] = per[p][0]
                    per[p][3]-=1
                    day[j] = "0"
                    per[p][1] = "{0},{1},{2},{3},{4}".format(day[0],day[1],day[2],day[3],day[4])
                    i = i+1
    #下午打三
    for j in range(5,10):
        i = 11
        random.shuffle(layer)
        l = -1
        while i!=12:
            l += 1
            if l == line:
                break
            p = layer[l]
            per[p][7] = str(per[p][7])
            if per[p][7] == "1":
                if ros[j][i] !=0:
                    break
                day = []
                d = per[p][2]
                day = list(d.split(","))    
                per[p][7] = int(per[p][7])
                per[p][3] = int(per[p][3])
                if day[j-5] != "0":
                    ros[j][i] = per[p][0]
                    per[p][3]-=1
                    day[j-5] = "0"
                    per[p][2] = "{0},{1},{2},{3},{4}".format(day[0],day[1],day[2],day[3],day[4])
                    i = i+1
    #上午北管
    for j in range(0,5):
        i = 5
        random.shuffle(layer)
        l = -1
        p1 = 1234
        while i!=7:
            l += 1
            if l == line:
                break
            p = layer[l]
            if p == p1:
                continue
            per[p][7] = str(per[p][7])
            if per[p][7] == "1":
                if ros[j][i] !=0:
                    break
                day = []
                d = per[p][1]
                day = list(d.split(","))    
                per[p][7] = int(per[p][7])
                per[p][3] = int(per[p][3])
                if day[j] != "0":
                    ros[j][i] = per[p][0]
                    per[p][3]-=1
                    day[j] = "0"
                    per[p][1] = "{0},{1},{2},{3},{4}".format(day[0],day[1],day[2],day[3],day[4])
                    i = i+1
                    p1 = p
    #下午北管
    for j in range(5,10):
        i = 5
        random.shuffle(layer)
        l = -1
        p1 = 1234
        while i!=7:
            l += 1
            if l == line:
                break
            p = layer[l]
            if p == p1:
                continue        
            per[p][7] = str(per[p][7])
            if per[p][7] == "1":
                if ros[j][i] !=0:
                    break
                day = []
                d = per[p][2]
                day = list(d.split(","))    
                per[p][7] = int(per[p][7])
                per[p][3] = int(per[p][3])
                if day[j-5] != "0":
                    ros[j][i] = per[p][0]
                    per[p][3]-=1
                    day[j-5] = "0"
                    per[p][2] = "{0},{1},{2},{3},{4}".format(day[0],day[1],day[2],day[3],day[4])
                    i = i+1
                    p1 = p
    #早上二打
    for j in range(0,5):
        i = 7
        random.shuffle(layer)
        l = -1
        p1 = 1234
        while i!=9:
            l += 1
            if l == line:
                break
            p = layer[l]
            if p == p1:
                continue
            if per[p][4] != "1":
                if ros[j][i] !=0:
                    break
                day = []
                d = per[p][1]
                day = list(d.split(","))    
                per[p][4] = int(per[p][4])
                per[p][3] = int(per[p][3])
                if day[j] != "0":
                    ros[j][i] = per[p][0]
                    per[p][3]-=1
                    day[j] = "0"
                    per[p][1] = "{0},{1},{2},{3},{4}".format(day[0],day[1],day[2],day[3],day[4])
                    i = i+1
                    p1 = p
    #下午二打
    for j in range(5,10):
        i = 7
        random.shuffle(layer)
        l = -1
        p1 = 1234
        while i!=9:
            l += 1
            if l == line:
                break
            p = layer[l]
            if p == p1:
                continue
            if per[p][4] != "1":
                if ros[j][i] !=0:
                    break
                day = []
                d = per[p][2]
                day = list(d.split(","))    
                per[p][4] = int(per[p][4])
                per[p][3] = int(per[p][3])
                if day[j-5] != "0":
                    ros[j][i] = per[p][0]
                    per[p][3]-=1
                    day[j-5] = "0"
                    per[p][2] = "{0},{1},{2},{3},{4}".format(day[0],day[1],day[2],day[3],day[4])
                    i = i+1
                    p1 = p
    #上午大檔
    for j in range(0,5):
        i = 3
        random.shuffle(layer)
        l = -1
        p1 = 1234
        while i!=5:
            l += 1
            if l == line:
                break
            p = layer[l]
            if p == p1:
                continue
            if per[p][4] != "1":
                if ros[j][i] !=0:
                    break
                day = []
                d = per[p][1]
                day = list(d.split(","))    
                per[p][4] = int(per[p][4])
                per[p][3] = int(per[p][3])
                if day[j] != "0":
                    ros[j][i] = per[p][0]
                    per[p][3]-=1
                    day[j] = "0"
                    per[p][1] = "{0},{1},{2},{3},{4}".format(day[0],day[1],day[2],day[3],day[4])
                    i = i+1
                    p1 = p
    #下午大檔
    for j in range(5,10):
        i = 3
        random.shuffle(layer)
        l = -1
        p1 = 1234
        while i!=5:
            l += 1
            if l == line:
                break
            p = layer[l]
            if p == p1:
                continue
            if per[p][4] != "1":
                if ros[j][i] !=0:
                    break
                day = []
                d = per[p][2]
                day = list(d.split(","))    
                per[p][4] = int(per[p][4])
                per[p][3] = int(per[p][3])
                if day[j-5] != "0":
                    ros[j][i] = per[p][0]
                    per[p][3]-=1
                    day[j-5] = "0"
                    per[p][2] = "{0},{1},{2},{3},{4}".format(day[0],day[1],day[2],day[3],day[4])
                    i = i+1
                    p1 = p
    #上午魯班
    for j in range(0,5):
        i = 1
        random.shuffle(layer)
        l = -1
        p1 = 1234
        while i!=3:
            l += 1
            if l == line:
                break
            p = layer[l]
            if p == p1:
                continue
            if per[p][4] != "1":
                if ros[j][i] !=0:
                    break
                day = []
                d = per[p][1]
                day = list(d.split(","))    
                per[p][4] = int(per[p][4])
                per[p][3] = int(per[p][3])
                if day[j] != "0":
                    ros[j][i] = per[p][0]
                    per[p][3]-=1
                    day[j] = "0"
                    per[p][1] = "{0},{1},{2},{3},{4}".format(day[0],day[1],day[2],day[3],day[4])
                    i = i+1
                    p1 = p
    #下午魯班
    for j in range(5,10):
        i = 1
        random.shuffle(layer)
        l = -1
        p1 = 1234
        while i!=3:
            l += 1
            if l == line:
                break
            p = layer[l]
            p = random.randrange(0,line)
            if p == p1:
                continue
            if per[p][4] != "1":
                if ros[j][i] !=0:
                    break
                day = []
                d = per[p][2]
                day = list(d.split(","))    
                per[p][4] = int(per[p][4])
                per[p][3] = int(per[p][3])
                if day[j-5] != "0":
                    ros[j][i] = per[p][0]
                    per[p][3]-=1
                    day[j-5] = "0"
                    per[p][2] = "{0},{1},{2},{3},{4}".format(day[0],day[1],day[2],day[3],day[4])
                    i = i+1
                    p1 = p
    #二線
    for j in range(0,5):
        i = 0
        random.shuffle(layer)
        l = -1
        while i!=1:
            l += 1
            if l == line:
                break
            p = layer[l]
            if per[p][4] != "1":
                if ros[j][i] !=0:
                    break
                day = []
                d = per[p][1]
                day = list(d.split(","))
                per[p][3] = int(per[p][3])
                if day[j] != "0":
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
    btn0big.place_forget()
    btn1big.place_forget()
    btn2big.place_forget()
    btn3big.place_forget()
    btn4big.place_forget()
    btn5big.place_forget()
    btn6big.place_forget()
    btn7big.place_forget()
    btn8big.place_forget()
    btn9big.place_forget()
    btn0two.place_forget()
    btn1two.place_forget()
    btn2two.place_forget()
    btn3two.place_forget()
    btn4two.place_forget()
    btn5two.place_forget()
    btn6two.place_forget()
    btn7two.place_forget()
    btn8two.place_forget()
    btn9two.place_forget()
    btn0three.place_forget()
    btn1three.place_forget()
    btn2three.place_forget()
    btn3three.place_forget()
    btn4three.place_forget()
    btn5three.place_forget()
    btn6three.place_forget()
    btn7three.place_forget()
    btn8three.place_forget()
    btn9three.place_forget()
    btn0right1.place_forget()
    btn1right1.place_forget()
    btn2right1.place_forget()
    btn3right1.place_forget()
    btn4right1.place_forget()
    btn5right1.place_forget()
    btn6right1.place_forget()
    btn7right1.place_forget()
    btn8right1.place_forget()
    btn9right1.place_forget()
    btn0right2.place_forget()
    btn1right2.place_forget()
    btn2right2.place_forget()
    btn3right2.place_forget()
    btn4right2.place_forget()
    btn5right2.place_forget()
    btn6right2.place_forget()
    btn7right2.place_forget()
    btn8right2.place_forget()
    btn9right2.place_forget()
    btn0right11.place_forget()
    btn1right11.place_forget()
    btn2right11.place_forget()
    btn3right11.place_forget()
    btn4right11.place_forget()
    btn5right11.place_forget()
    btn6right11.place_forget()
    btn7right11.place_forget()
    btn8right11.place_forget()
    btn9right11.place_forget()
    btn0right22.place_forget()
    btn1right22.place_forget()
    btn2right22.place_forget()
    btn3right22.place_forget()
    btn4right22.place_forget()
    btn5right22.place_forget()
    btn6right22.place_forget()
    btn7right22.place_forget()
    btn8right22.place_forget()
    btn9right22.place_forget()
    btn0right13.place_forget()
    btn1right13.place_forget()
    btn2right13.place_forget()
    btn3right13.place_forget()
    btn4right13.place_forget()
    btn5right13.place_forget()
    btn6right13.place_forget()
    btn7right13.place_forget()
    btn8right13.place_forget()
    btn9right13.place_forget()
    btn0right23.place_forget()
    btn1right23.place_forget()
    btn2right23.place_forget()
    btn3right23.place_forget()
    btn4right23.place_forget()
    btn5right23.place_forget()
    btn6right23.place_forget()
    btn7right23.place_forget()
    btn8right23.place_forget()
    btn9right23.place_forget()
    btn0right14.place_forget()
    btn1right14.place_forget()
    btn2right14.place_forget()
    btn3right14.place_forget()
    btn4right14.place_forget()
    btn5right14.place_forget()
    btn6right14.place_forget()
    btn7right14.place_forget()
    btn8right14.place_forget()
    btn9right14.place_forget()
    btn0right24.place_forget()
    btn1right24.place_forget()
    btn2right24.place_forget()
    btn3right24.place_forget()
    btn4right24.place_forget()
    btn5right24.place_forget()
    btn6right24.place_forget()
    btn7right24.place_forget()
    btn8right24.place_forget()
    btn9right24.place_forget()
    btn0right15.place_forget()
    btn1right15.place_forget()
    btn2right15.place_forget()
    btn3right15.place_forget()
    btn4right15.place_forget()
    btn5right15.place_forget()
    btn6right15.place_forget()
    btn7right15.place_forget()
    btn8right15.place_forget()
    btn9right15.place_forget()
    btn0right25.place_forget()
    btn1right25.place_forget()
    btn2right25.place_forget()
    btn3right25.place_forget()
    btn4right25.place_forget()
    btn5right25.place_forget()
    btn6right25.place_forget()
    btn7right25.place_forget()
    btn8right25.place_forget()
    btn9right25.place_forget()
    btn0right26.place_forget()
    btn1right26.place_forget()
    btn2right26.place_forget()
    btn3right26.place_forget()
    btn4right26.place_forget()
    btn5right26.place_forget()
    btn6right26.place_forget()
    btn7right26.place_forget()
    btn8right26.place_forget()
    btn9right26.place_forget()
def change_label_numer(pc1,pc2):
    global per,line,ros,dd,cc
    dd = pc1
    cc = pc2
    txt.set("目前選擇:"+str(car[cc])+str(day[dd]))
def lastc():
    global dd,cc,ctext,cancel
    if ros[dd][cc]!=0:
        cancel = 1
    name = listbox.curselection()
    if(int(sum(name)) == line):
        ros[dd][cc] = 0
        ctext[dd][cc].set(day[dd])
        cancel = 0
        if ros[dd][cc] != 0:
            per[sum(name)][3] = int(per[sum(name)][3])
            per[sum(name)][3] += 1
            if(dd<5):
                da = []
                d = per[sum(name)][1]
                da = list(d.split(","))
                da[dd] = str(dd)
                per[sum(name)][1] = "{0},{1},{2},{3},{4}".format(da[0],da[1],da[2],da[3],da[4])
            else:
                da = []
                d = per[sum(name)][2]
                da = list(d.split(","))
                da[dd-5] = str(dd-5)
                per[sum(name)][2] = "{0},{1},{2},{3},{4}".format(da[0],da[1],da[2],da[3],da[4])
            if cc==10 or cc==11:
                per[sum(name)][6] = int(per[sum(name)][6])
                per[sum(name)][6] += 1
            txt.set("目前選擇:"+str(car[cc])+str(day[dd]))
    elif cancel == 0:
        ros[dd][cc] = per[sum(name)][0]
        ctext[dd][cc].set(per[sum(name)][0])
        per[sum(name)][3] = int(per[sum(name)][3])
        per[sum(name)][3] -= 1
        if(dd<5):
            da = []
            d = per[sum(name)][1]
            da = list(d.split(","))
            da[dd] = "0"
            per[sum(name)][1] = "{0},{1},{2},{3},{4}".format(da[0],da[1],da[2],da[3],da[4])
        else:
            da = []
            d = per[sum(name)][2]
            da = list(d.split(","))
            da[dd-5] = "0"
            per[sum(name)][2] = "{0},{1},{2},{3},{4}".format(da[0],da[1],da[2],da[3],da[4])
        if cc==10 or cc==11:
            per[sum(name)][6] = int(per[sum(name)][6])
            per[sum(name)][6] -= 1
        txt.set("目前選擇:"+str(car[cc])+str(day[dd]))
    elif cancel == 1:
        txt.set("請先取消再更改，取消在最下層")
#--------------------------------------------tkinter
win=tk.Tk()
win.geometry("957x740")
style = ttk.Style(win)
style.configure('Calendar.Treeview', rowheight=40)
tree=ttk.Treeview(win,style = 'Calendar.Treeview')#表格
tree["columns"]=("二線","魯班","大檔","北管","二打","正打","打三","二燈","大燈")
#表示列,不顯示
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
tree.heading("魯班",text="魯班")  #顯示表頭
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
layer = []
for i in range(0,line):
    layer.append(i)
#--------------------------------------------
choice = tk.IntVar()
lab = tk.Label(win,text="按按鈕排班")
lab.pack()
btn = tk.Button(win,text="開始",command = start)
btn.pack()

#--------------------------------------------change
dd = 0
cc = 0
cancel = 0
ros = [[0] *14 for i in range(10)]
ctext = [[0] *14 for i in range(10)]
for i in range(10):
    if i==0:
        for j in range(14):
            ctext[i][j] = tk.StringVar()
            ctext[i][j].set("一上")
    if i==5:
        for j in range(14):
            ctext[i][j] = tk.StringVar()
            ctext[i][j].set("一下")
    if i==1:
        for j in range(14):
            ctext[i][j] = tk.StringVar()
            ctext[i][j].set("二上")
    if i==6:
        for j in range(14):
            ctext[i][j] = tk.StringVar()
            ctext[i][j].set("二下")
    if i==2:
        for j in range(14):
            ctext[i][j] = tk.StringVar()
            ctext[i][j].set("三上")
    if i==7:
        for j in range(14):
            ctext[i][j] = tk.StringVar()
            ctext[i][j].set("三下")
    if i==3:
        for j in range(14):
            ctext[i][j] = tk.StringVar()
            ctext[i][j].set("四上")
    if i==8:
        for j in range(14):
            ctext[i][j] = tk.StringVar()
            ctext[i][j].set("四下")
    if i==4:
        for j in range(14):
            ctext[i][j] = tk.StringVar()
            ctext[i][j].set("五上")
    if i==9:
        for j in range(14):
            ctext[i][j] = tk.StringVar()
            ctext[i][j].set("五下")
#大燈----------------------------------------
btn0big = tk.Button(win,textvariable = ctext[0][13],command = partial(change_label_numer, 0,13))
btn0big.place(x=905,y=80)
btn5big = tk.Button(win,textvariable = ctext[5][13],command = partial(change_label_numer, 5,13))
btn5big.place(x=905,y=120)
btn1big = tk.Button(win,textvariable = ctext[1][13],command = partial(change_label_numer, 1,13))
btn1big.place(x=905,y=160)
btn6big = tk.Button(win,textvariable = ctext[6][13],command = partial(change_label_numer, 6,13))
btn6big.place(x=905,y=200)
btn2big = tk.Button(win,textvariable = ctext[2][13],command = partial(change_label_numer, 2,13))
btn2big.place(x=905,y=240)
btn7big = tk.Button(win,textvariable = ctext[7][13],command = partial(change_label_numer, 7,13))
btn7big.place(x=905,y=280)
btn3big = tk.Button(win,textvariable = ctext[3][13],command = partial(change_label_numer, 3,13))
btn3big.place(x=905,y=320)
btn8big = tk.Button(win,textvariable = ctext[8][13],command = partial(change_label_numer, 8,13))
btn8big.place(x=905,y=360)
btn4big = tk.Button(win,textvariable = ctext[4][13],command = partial(change_label_numer, 4,13))
btn4big.place(x=905,y=400)
btn9big = tk.Button(win,textvariable = ctext[9][13],command = partial(change_label_numer, 9,13))
btn9big.place(x=905,y=440)
#--------------------------------------------二燈
btn0two = tk.Button(win,textvariable = ctext[0][12],command = partial(change_label_numer, 0,12))
btn0two.place(x=858,y=80)
btn5two = tk.Button(win,textvariable = ctext[5][12],command = partial(change_label_numer, 5,12))
btn5two.place(x=858,y=120)
btn1two = tk.Button(win,textvariable = ctext[1][12],command = partial(change_label_numer, 1,12))
btn1two.place(x=858,y=160)
btn6two = tk.Button(win,textvariable = ctext[6][12],command = partial(change_label_numer, 6,12))
btn6two.place(x=858,y=200)
btn2two = tk.Button(win,textvariable = ctext[2][12],command = partial(change_label_numer, 2,12))
btn2two.place(x=858,y=240)
btn7two = tk.Button(win,textvariable = ctext[7][12],command = partial(change_label_numer, 7,12))
btn7two.place(x=858,y=280)
btn3two = tk.Button(win,textvariable = ctext[3][12],command = partial(change_label_numer, 3,12))
btn3two.place(x=858,y=320)
btn8two = tk.Button(win,textvariable = ctext[8][12],command = partial(change_label_numer, 8,12))
btn8two.place(x=858,y=360)
btn4two = tk.Button(win,textvariable = ctext[4][12],command = partial(change_label_numer, 4,12))
btn4two.place(x=858,y=400)
btn9two = tk.Button(win,textvariable = ctext[9][12],command = partial(change_label_numer, 9,12))
btn9two.place(x=858,y=440)
#--------------------------------------------打三
btn0three = tk.Button(win,textvariable = ctext[0][11],command = partial(change_label_numer, 0,11))
btn0three.place(x=811,y=80)
btn5three = tk.Button(win,textvariable = ctext[5][11],command = partial(change_label_numer, 5,11))
btn5three.place(x=811,y=120)
btn1three = tk.Button(win,textvariable = ctext[1][11],command = partial(change_label_numer, 1,11))
btn1three.place(x=811,y=160)
btn6three = tk.Button(win,textvariable = ctext[6][11],command = partial(change_label_numer, 6,11))
btn6three.place(x=811,y=200)
btn2three = tk.Button(win,textvariable = ctext[2][11],command = partial(change_label_numer, 2,11))
btn2three.place(x=811,y=240)
btn7three = tk.Button(win,textvariable = ctext[7][11],command = partial(change_label_numer, 7,11))
btn7three.place(x=811,y=280)
btn3three = tk.Button(win,textvariable = ctext[3][11],command = partial(change_label_numer, 3,11))
btn3three.place(x=811,y=320)
btn8three = tk.Button(win,textvariable = ctext[8][11],command = partial(change_label_numer, 8,11))
btn8three.place(x=811,y=360)
btn4three = tk.Button(win,textvariable = ctext[4][11],command = partial(change_label_numer, 4,11))
btn4three.place(x=811,y=400)
btn9three = tk.Button(win,textvariable = ctext[9][11],command = partial(change_label_numer, 9,11))
btn9three.place(x=811,y=440)
#-------------------------------------------正打
btn0right1 = tk.Button(win,textvariable = ctext[0][10],command = partial(change_label_numer, 0,10))
btn0right1.place(x=760,y=80)
btn5right1 = tk.Button(win,textvariable = ctext[5][10],command = partial(change_label_numer, 5,10))
btn5right1.place(x=760,y=120)
btn1right1 = tk.Button(win,textvariable = ctext[1][10],command = partial(change_label_numer, 1,10))
btn1right1.place(x=760,y=160)
btn6right1 = tk.Button(win,textvariable = ctext[6][10],command = partial(change_label_numer, 6,10))
btn6right1.place(x=760,y=200)
btn2right1 = tk.Button(win,textvariable = ctext[2][10],command = partial(change_label_numer, 2,10))
btn2right1.place(x=760,y=240)
btn7right1 = tk.Button(win,textvariable = ctext[7][10],command = partial(change_label_numer, 7,10))
btn7right1.place(x=760,y=280)
btn3right1 = tk.Button(win,textvariable = ctext[3][10],command = partial(change_label_numer, 3,10))
btn3right1.place(x=760,y=320)
btn8right1 = tk.Button(win,textvariable = ctext[8][10],command = partial(change_label_numer, 8,10))
btn8right1.place(x=760,y=360)
btn4right1 = tk.Button(win,textvariable = ctext[4][10],command = partial(change_label_numer, 4,10))
btn4right1.place(x=760,y=400)
btn9right1 = tk.Button(win,textvariable = ctext[9][10],command = partial(change_label_numer, 9,10))
btn9right1.place(x=760,y=440)
#--------------------------------------------
btn0right2 = tk.Button(win,textvariable = ctext[0][9],command = partial(change_label_numer, 0,9))
btn0right2.place(x=710,y=80)
btn5right2 = tk.Button(win,textvariable = ctext[5][9],command = partial(change_label_numer, 5,9))
btn5right2.place(x=710,y=120)
btn1right2 = tk.Button(win,textvariable = ctext[1][9],command = partial(change_label_numer, 1,9))
btn1right2.place(x=710,y=160)
btn6right2 = tk.Button(win,textvariable = ctext[6][9],command = partial(change_label_numer, 6,9))
btn6right2.place(x=710,y=200)
btn2right2 = tk.Button(win,textvariable = ctext[2][9],command = partial(change_label_numer, 2,9))
btn2right2.place(x=710,y=240)
btn7right2 = tk.Button(win,textvariable = ctext[7][9],command = partial(change_label_numer, 7,9))
btn7right2.place(x=710,y=280)
btn3right2 = tk.Button(win,textvariable = ctext[3][9],command = partial(change_label_numer, 3,9))
btn3right2.place(x=710,y=320)
btn8right2 = tk.Button(win,textvariable = ctext[8][9],command = partial(change_label_numer, 8,9))
btn8right2.place(x=710,y=360)
btn4right2 = tk.Button(win,textvariable = ctext[4][9],command = partial(change_label_numer, 4,9))
btn4right2.place(x=710,y=400)
btn9right2 = tk.Button(win,textvariable = ctext[9][9],command = partial(change_label_numer, 9,9))
btn9right2.place(x=710,y=440)
#--------------------------------------------二打
btn0right11 = tk.Button(win,textvariable = ctext[0][8],command = partial(change_label_numer, 0,8))
btn0right11.place(x=660,y=80)
btn5right11 = tk.Button(win,textvariable = ctext[5][8],command = partial(change_label_numer, 5,8))
btn5right11.place(x=660,y=120)
btn1right11 = tk.Button(win,textvariable = ctext[1][8],command = partial(change_label_numer, 1,8))
btn1right11.place(x=660,y=160)
btn6right11 = tk.Button(win,textvariable = ctext[6][8],command = partial(change_label_numer, 6,8))
btn6right11.place(x=660,y=200)
btn2right11 = tk.Button(win,textvariable = ctext[2][8],command = partial(change_label_numer, 2,8))
btn2right11.place(x=660,y=240)
btn7right11 = tk.Button(win,textvariable = ctext[7][8],command = partial(change_label_numer, 7,8))
btn7right11.place(x=660,y=280)
btn3right11 = tk.Button(win,textvariable = ctext[3][8],command = partial(change_label_numer, 3,8))
btn3right11.place(x=660,y=320)
btn8right11 = tk.Button(win,textvariable = ctext[8][8],command = partial(change_label_numer, 8,8))
btn8right11.place(x=660,y=360)
btn4right11 = tk.Button(win,textvariable = ctext[4][8],command = partial(change_label_numer, 4,8))
btn4right11.place(x=660,y=400)
btn9right11 = tk.Button(win,textvariable = ctext[9][8],command = partial(change_label_numer, 9,8))
btn9right11.place(x=660,y=440)
#--------------------------------------------
btn0right22 = tk.Button(win,textvariable = ctext[0][7],command = partial(change_label_numer, 0,7))
btn0right22.place(x=610,y=80)
btn5right22 = tk.Button(win,textvariable = ctext[5][7],command = partial(change_label_numer, 5,7))
btn5right22.place(x=610,y=120)
btn1right22 = tk.Button(win,textvariable = ctext[1][7],command = partial(change_label_numer, 1,7))
btn1right22.place(x=610,y=160)
btn6right22 = tk.Button(win,textvariable = ctext[6][7],command = partial(change_label_numer, 6,7))
btn6right22.place(x=610,y=200)
btn2right22 = tk.Button(win,textvariable = ctext[2][7],command = partial(change_label_numer, 2,7))
btn2right22.place(x=610,y=240)
btn7right22 = tk.Button(win,textvariable = ctext[7][7],command = partial(change_label_numer, 7,7))
btn7right22.place(x=610,y=280)
btn3right22 = tk.Button(win,textvariable = ctext[3][7],command = partial(change_label_numer, 3,7))
btn3right22.place(x=610,y=320)
btn8right22 = tk.Button(win,textvariable = ctext[8][7],command = partial(change_label_numer, 8,7))
btn8right22.place(x=610,y=360)
btn4right22 = tk.Button(win,textvariable = ctext[4][7],command = partial(change_label_numer, 4,7))
btn4right22.place(x=610,y=400)
btn9right22 = tk.Button(win,textvariable = ctext[9][7],command = partial(change_label_numer, 9,7))
btn9right22.place(x=610,y=440)
#--------------------------------------------北管
btn0right13 = tk.Button(win,textvariable = ctext[0][6],command = partial(change_label_numer, 0,6))
btn0right13.place(x=560,y=80)
btn5right13 = tk.Button(win,textvariable = ctext[5][6],command = partial(change_label_numer, 5,6))
btn5right13.place(x=560,y=120)
btn1right13 = tk.Button(win,textvariable = ctext[1][6],command = partial(change_label_numer, 1,6))
btn1right13.place(x=560,y=160)
btn6right13 = tk.Button(win,textvariable = ctext[6][6],command = partial(change_label_numer, 6,6))
btn6right13.place(x=560,y=200)
btn2right13 = tk.Button(win,textvariable = ctext[2][6],command = partial(change_label_numer, 2,6))
btn2right13.place(x=560,y=240)
btn7right13 = tk.Button(win,textvariable = ctext[7][6],command = partial(change_label_numer, 7,6))
btn7right13.place(x=560,y=280)
btn3right13 = tk.Button(win,textvariable = ctext[3][6],command = partial(change_label_numer, 3,6))
btn3right13.place(x=560,y=320)
btn8right13 = tk.Button(win,textvariable = ctext[8][6],command = partial(change_label_numer, 8,6))
btn8right13.place(x=560,y=360)
btn4right13 = tk.Button(win,textvariable = ctext[4][6],command = partial(change_label_numer, 4,6))
btn4right13.place(x=560,y=400)
btn9right13 = tk.Button(win,textvariable = ctext[9][6],command = partial(change_label_numer, 9,6))
btn9right13.place(x=560,y=440)
#--------------------------------------------
btn0right23 = tk.Button(win,textvariable = ctext[0][5],command = partial(change_label_numer, 0,5))
btn0right23.place(x=510,y=80)
btn5right23 = tk.Button(win,textvariable = ctext[5][5],command = partial(change_label_numer, 5,5))
btn5right23.place(x=510,y=120)
btn1right23 = tk.Button(win,textvariable = ctext[1][5],command = partial(change_label_numer, 1,5))
btn1right23.place(x=510,y=160)
btn6right23 = tk.Button(win,textvariable = ctext[6][5],command = partial(change_label_numer, 6,5))
btn6right23.place(x=510,y=200)
btn2right23 = tk.Button(win,textvariable = ctext[2][5],command = partial(change_label_numer, 2,5))
btn2right23.place(x=510,y=240)
btn7right23 = tk.Button(win,textvariable = ctext[7][5],command = partial(change_label_numer, 7,5))
btn7right23.place(x=510,y=280)
btn3right23 = tk.Button(win,textvariable = ctext[3][5],command = partial(change_label_numer, 3,5))
btn3right23.place(x=510,y=320)
btn8right23 = tk.Button(win,textvariable = ctext[8][5],command = partial(change_label_numer, 8,5))
btn8right23.place(x=510,y=360)
btn4right23 = tk.Button(win,textvariable = ctext[4][5],command = partial(change_label_numer, 4,5))
btn4right23.place(x=510,y=400)
btn9right23 = tk.Button(win,textvariable = ctext[9][5],command = partial(change_label_numer, 9,5))
btn9right23.place(x=510,y=440)
#--------------------------------------------大檔
btn0right14 = tk.Button(win,textvariable = ctext[0][4],command = partial(change_label_numer, 0,4))
btn0right14.place(x=460,y=80)
btn5right14 = tk.Button(win,textvariable = ctext[5][4],command = partial(change_label_numer, 5,4))
btn5right14.place(x=460,y=120)
btn1right14 = tk.Button(win,textvariable = ctext[1][4],command = partial(change_label_numer, 1,4))
btn1right14.place(x=460,y=160)
btn6right14 = tk.Button(win,textvariable = ctext[6][4],command = partial(change_label_numer, 6,4))
btn6right14.place(x=460,y=200)
btn2right14 = tk.Button(win,textvariable = ctext[2][4],command = partial(change_label_numer, 2,4))
btn2right14.place(x=460,y=240)
btn7right14 = tk.Button(win,textvariable = ctext[7][4],command = partial(change_label_numer, 7,4))
btn7right14.place(x=460,y=280)
btn3right14 = tk.Button(win,textvariable = ctext[3][4],command = partial(change_label_numer, 3,4))
btn3right14.place(x=460,y=320)
btn8right14 = tk.Button(win,textvariable = ctext[8][4],command = partial(change_label_numer, 8,4))
btn8right14.place(x=460,y=360)
btn4right14 = tk.Button(win,textvariable = ctext[4][4],command = partial(change_label_numer, 4,4))
btn4right14.place(x=460,y=400)
btn9right14 = tk.Button(win,textvariable = ctext[9][4],command = partial(change_label_numer, 9,4))
btn9right14.place(x=460,y=440)
#--------------------------------------------
btn0right24 = tk.Button(win,textvariable = ctext[0][3],command = partial(change_label_numer, 0,3))
btn0right24.place(x=410,y=80)
btn5right24 = tk.Button(win,textvariable = ctext[5][3],command = partial(change_label_numer, 5,3))
btn5right24.place(x=410,y=120)
btn1right24 = tk.Button(win,textvariable = ctext[1][3],command = partial(change_label_numer, 1,3))
btn1right24.place(x=410,y=160)
btn6right24 = tk.Button(win,textvariable = ctext[6][3],command = partial(change_label_numer, 6,3))
btn6right24.place(x=410,y=200)
btn2right24 = tk.Button(win,textvariable = ctext[2][3],command = partial(change_label_numer, 2,3))
btn2right24.place(x=410,y=240)
btn7right24 = tk.Button(win,textvariable = ctext[7][3],command = partial(change_label_numer, 7,3))
btn7right24.place(x=410,y=280)
btn3right24 = tk.Button(win,textvariable = ctext[3][3],command = partial(change_label_numer, 3,3))
btn3right24.place(x=410,y=320)
btn8right24 = tk.Button(win,textvariable = ctext[8][3],command = partial(change_label_numer, 8,3))
btn8right24.place(x=410,y=360)
btn4right24 = tk.Button(win,textvariable = ctext[4][3],command = partial(change_label_numer, 4,3))
btn4right24.place(x=410,y=400)
btn9right24 = tk.Button(win,textvariable = ctext[9][3],command = partial(change_label_numer, 9,3))
btn9right24.place(x=410,y=440)
#--------------------------------------------魯班
btn0right15 = tk.Button(win,textvariable = ctext[0][2],command = partial(change_label_numer, 0,2))
btn0right15.place(x=360,y=80)
btn5right15 = tk.Button(win,textvariable = ctext[5][2],command = partial(change_label_numer, 5,2))
btn5right15.place(x=360,y=120)
btn1right15 = tk.Button(win,textvariable = ctext[1][2],command = partial(change_label_numer, 1,2))
btn1right15.place(x=360,y=160)
btn6right15 = tk.Button(win,textvariable = ctext[6][2],command = partial(change_label_numer, 6,2))
btn6right15.place(x=360,y=200)
btn2right15 = tk.Button(win,textvariable = ctext[2][2],command = partial(change_label_numer, 2,2))
btn2right15.place(x=360,y=240)
btn7right15 = tk.Button(win,textvariable = ctext[7][2],command = partial(change_label_numer, 7,2))
btn7right15.place(x=360,y=280)
btn3right15 = tk.Button(win,textvariable = ctext[3][2],command = partial(change_label_numer, 3,2))
btn3right15.place(x=360,y=320)
btn8right15 = tk.Button(win,textvariable = ctext[8][2],command = partial(change_label_numer, 8,2))
btn8right15.place(x=360,y=360)
btn4right15 = tk.Button(win,textvariable = ctext[4][2],command = partial(change_label_numer, 4,2))
btn4right15.place(x=360,y=400)
btn9right15 = tk.Button(win,textvariable = ctext[9][2],command = partial(change_label_numer, 9,2))
btn9right15.place(x=360,y=440)
#--------------------------------------------
btn0right25 = tk.Button(win,textvariable = ctext[0][1],command = partial(change_label_numer, 0,1))
btn0right25.place(x=310,y=80)
btn5right25 = tk.Button(win,textvariable = ctext[5][1],command = partial(change_label_numer, 5,1))
btn5right25.place(x=310,y=120)
btn1right25 = tk.Button(win,textvariable = ctext[1][1],command = partial(change_label_numer, 1,1))
btn1right25.place(x=310,y=160)
btn6right25 = tk.Button(win,textvariable = ctext[6][1],command = partial(change_label_numer, 6,1))
btn6right25.place(x=310,y=200)
btn2right25 = tk.Button(win,textvariable = ctext[2][1],command = partial(change_label_numer, 2,1))
btn2right25.place(x=310,y=240)
btn7right25 = tk.Button(win,textvariable = ctext[7][1],command = partial(change_label_numer, 7,1))
btn7right25.place(x=310,y=280)
btn3right25 = tk.Button(win,textvariable = ctext[3][1],command = partial(change_label_numer, 3,1))
btn3right25.place(x=310,y=320)
btn8right25 = tk.Button(win,textvariable = ctext[8][1],command = partial(change_label_numer, 8,1))
btn8right25.place(x=310,y=360)
btn4right25 = tk.Button(win,textvariable = ctext[4][1],command = partial(change_label_numer, 4,1))
btn4right25.place(x=310,y=400)
btn9right25 = tk.Button(win,textvariable = ctext[9][1],command = partial(change_label_numer, 9,1))
btn9right25.place(x=310,y=440)
#--------------------------------------------二線
btn0right26 = tk.Button(win,textvariable = ctext[0][0],command = partial(change_label_numer, 0,0))
btn0right26.place(x=210,y=80)
btn5right26 = tk.Button(win,textvariable = ctext[5][0],command = partial(change_label_numer, 5,0))
btn5right26.place(x=210,y=120)
btn1right26 = tk.Button(win,textvariable = ctext[1][0],command = partial(change_label_numer, 1,0))
btn1right26.place(x=210,y=160)
btn6right26 = tk.Button(win,textvariable = ctext[6][0],command = partial(change_label_numer, 6,0))
btn6right26.place(x=210,y=200)
btn2right26 = tk.Button(win,textvariable = ctext[2][0],command = partial(change_label_numer, 2,0))
btn2right26.place(x=210,y=240)
btn7right26 = tk.Button(win,textvariable = ctext[7][0],command = partial(change_label_numer, 7,0))
btn7right26.place(x=210,y=280)
btn3right26 = tk.Button(win,textvariable = ctext[3][0],command = partial(change_label_numer, 3,0))
btn3right26.place(x=210,y=320)
btn8right26 = tk.Button(win,textvariable = ctext[8][0],command = partial(change_label_numer, 8,0))
btn8right26.place(x=210,y=360)
btn4right26 = tk.Button(win,textvariable = ctext[4][0],command = partial(change_label_numer, 4,0))
btn4right26.place(x=210,y=400)
btn9right26 = tk.Button(win,textvariable = ctext[9][0],command = partial(change_label_numer, 9,0))
btn9right26.place(x=210,y=440)
#--------------------------------------------
txt = tk.StringVar()
txt.set("尚未選擇")
la = tk.Label(win,textvariable = txt,font = ("新細明體",20),fg = "red")
la.place(x=0,y=490)
listbox = tk.Listbox(win)
for i in range(line):
    listbox.insert(END,per[i][0])
listbox.insert(END,"取消")
listbox.place(x=410,y=500)
bt = tk.Button(win,text = "選擇",command = lastc)
bt.place(x=457,y=665)
day = ["一上","二上","三上","四上","五上","一下","二下","三下","四下","五下"]
car = ["二線","魯班","魯班","大檔","大檔","北管","北管","二打","二打","正打","正打","打三","二燈","大燈"]

tree.pack()
win.mainloop()

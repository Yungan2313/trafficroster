import tkinter as tk
from tkinter import END
from tkinter import Y
from  tkinter import ttk
from tkinter import Grid
from functools import partial

def delete():
    global line
    name = sum(listbox.curselection())
    listbox.delete(name)
    nu = line-name-1
    if nu != 0:
        for i in range(name,name+nu):
            for j in range(0,10):
                per[i][j] = per[i+1][j]
        del per[line-1:line]
        line = line-1
    else:
        del per[name:name+1]
        line = line-1
    edittxt = open("edit.txt","w",encoding="utf-8")
    for i in range(line):
        edittxt.write("{0} {1} {2} {3} {4} {5} {6} {7} {8} {9}\n".format(per[i][0],per[i][1],per[i][2],per[i][3],str(per[i][4]),str(per[i][5]),per[i][6],str(per[i][7]),str(per[i][8]),str(per[i][9])))
    edittxt.close()
def lastedit():
    global line,adedchange
    mo = []
    af = []
    day = ["0","1","2","3","4","5"]
    peredit[0] = ennatxt.get()
    for i in range(0,5):
        if permo[i] == 1:
            mo.append(i+1)
        else:
            mo.append(0)
    peredit[1] = str(day[mo[0]])+","+str(day[mo[1]])+","+str(day[mo[2]])+","+str(day[mo[3]])+","+str(day[mo[4]])
    for i in range(0,5):
        if peraf[i] == 1:
            af.append(i+1)
        else:
            af.append(0)
    peredit[2] = str(day[af[0]])+","+str(day[af[1]])+","+str(day[af[2]])+","+str(day[af[3]])+","+str(day[af[4]])
    peredit[3] = entimetxt.get()
    if persen[0] == 0:
        peredit[4] = 0
    else:
        peredit[4] = 1
    if perright[0] == 0:
        peredit[5] = 0
    else:
        peredit[5] = 1
    peredit[6] = enrighttxt.get()
    if perback[0] == 0:
        peredit[7] = 0
    else:
        peredit[7] = 1
    if pertwo[0] == 0:
        peredit[8] = 0
    else:
        peredit[8] = 1
    if perbig[0] == 0:
        peredit[9] = 0
    else:
        peredit[9] = 1
        print(adedchange)
    if adedchange == 0:    
        for i in range(0,10):
            per[name][i] = peredit[i]
    else:
        line = line+1
        per.append(peredit)
        tree.insert("",0,text="資料" ,values=("none"))     
    edittxt = open("edit.txt","w",encoding="utf-8")
    for i in range(line):
        edittxt.write("{0} {1} {2} {3} {4} {5} {6} {7} {8} {9}\n".format(per[i][0],per[i][1],per[i][2],per[i][3],str(per[i][4]),str(per[i][5]),per[i][6],str(per[i][7]),str(per[i][8]),str(per[i][9])))
    edittxt.close()
        

def change_label_numer(dd):
    if dd<10:
        a = [btnm1,btntu1,btnw1,btnth1,btnf1,btnm2,btntu2,btnw2,btnth2,btnf2]
        b = a[dd]
        if c[dd] == 0:
            b.configure(bg = "red",fg = "white")
        else:
            b.configure(fg = "black",bg = 'gray93')
    elif dd>9 and dd<12:
        if dd==10:
            btnsenn.configure(bg = "red",fg = "white")
            btnseny.configure(fg = "black",bg = 'gray93')
        else:
            btnseny.configure(bg = "red",fg = "white")
            btnsenn.configure(fg = "black",bg = 'gray93')
    elif dd>11 and dd<14:
        if dd==12:
            btnrighty.configure(bg = "red",fg = "white")
            btnrightn.configure(fg = "black",bg = 'gray93')
        else:
            btnrightn.configure(bg = "red",fg = "white")
            btnrighty.configure(fg = "black",bg = 'gray93')
    elif dd>13 and dd<16:
        if dd==14:
            btntwoy.configure(bg = "red",fg = "white")
            btntwon.configure(fg = "black",bg = 'gray93')
        else:
            btntwon.configure(bg = "red",fg = "white")
            btntwoy.configure(fg = "black",bg = 'gray93')
    elif dd>15 and dd<18:
        if dd==16:
            btnbigy.configure(bg = "red",fg = "white")
            btnbign.configure(fg = "black",bg = 'gray93')
        else:
            btnbign.configure(bg = "red",fg = "white")
            btnbigy.configure(fg = "black",bg = 'gray93')
    elif dd>17 and dd<20:
        if dd==16:
            btnbacky.configure(bg = "red",fg = "white")
            btnbackn.configure(fg = "black",bg = 'gray93')
        else:
            btnbackn.configure(bg = "red",fg = "white")
            btnbacky.configure(fg = "black",bg = 'gray93')
    if dd<10:
        a = [btnm1,btntu1,btnw1,btnth1,btnf1,btnm2,btntu2,btnw2,btnth2,btnf2]
        b = a[dd]
        if c[dd] == 0:
            c[dd] = 1
            if dd<5:
                permo[dd] = 1
            else:
                peraf[dd-5] = 1
        else:
            c[dd] = 0
            if dd<5:
                permo[dd] = 0
            else:
                peraf[dd-5] = 0
    elif dd>9 and dd<12:
        if dd==10:
            persen[0] = 0
        else:
            persen[0] = 1
    elif dd>11 and dd<14:
        if dd==12:
            perright[0] = 1
        else:
            perright[0] = 0
    elif dd>13 and dd<16:
        if dd==14:
            pertwo[0] = 1
        else:
            pertwo[0] = 0
    elif dd>15 and dd<18:
        if dd==16:
            perbig[0] = 1
        else:
            perbig[0] = 0
    elif dd>17 and dd<20:
        if dd==16:
            perback[0] = 1
        else:
            perback[0] = 0

def choose():
    global name,adedchange
    m = [btnm1,btntu1,btnw1,btnth1,btnf1]
    a = [btnm2,btntu2,btnw2,btnth2,btnf2]
    name = sum(listbox.curselection())
    selected_item = tree.get_children() ## get selected item
    tree.delete(selected_item)
    daym = []
    daya = []
    day = ["","一","二","三","四","五"]
    dm = per[name][1]
    da = per[name][2]
    daym = list(dm.split(",")) 
    daya = list(da.split(","))
    daymtxt = str(day[int(daym[0])])+str(day[int(daym[1])])+str(day[int(daym[2])])+str(day[int(daym[3])])+str(day[int(daym[4])])
    dayatxt = str(day[int(daya[0])])+str(day[int(daya[1])])+str(day[int(daya[2])])+str(day[int(daya[3])])+str(day[int(daya[4])])
    if per[name][5] == "1":
        senbi = "是"
    else:
        senbi = "否"
    tree.insert("",0,text="資料" ,values=("{0}".format(per[name][0]),"{0}".format(daymtxt),"{0}".format(dayatxt),"{0}".format(per[name][3]),"{0}".format(senbi),"{0}".format(per[name][5]),"{0}".format(per[name][6]),"{0}".format(per[name][7]),"{0}".format(per[name][8])))
    for i in range(0,5):
        if daym[i]!="0":
            m[i].configure(bg = "red",fg = "white")
        else:
            m[i].configure(fg = "black",bg = 'gray93')
    for i in range(0,5):
        if daya[i]!="0":
            a[i].configure(bg = "red",fg = "white")
        else:
            a[i].configure(fg = "black",bg = 'gray93')
    if str(per[name][4]) == "0":
        btnsenn.configure(bg = "red",fg = "white")
        btnseny.configure(fg = "black",bg = 'gray93')
    else:
        btnseny.configure(bg = "red",fg = "white")
        btnsenn.configure(fg = "black",bg = 'gray93')
    if str(per[name][5]) == "0":
        btnrightn.configure(bg = "red",fg = "white")
        btnrighty.configure(fg = "black",bg = 'gray93')
    else:
        btnrighty.configure(bg = "red",fg = "white")
        btnrightn.configure(fg = "black",bg = 'gray93')
    if str(per[name][7]) == "0":
        btnbackn.configure(bg = "red",fg = "white")
        btnbacky.configure(fg = "black",bg = 'gray93')
    else:
        btnbacky.configure(bg = "red",fg = "white")
        btnbackn.configure(fg = "black",bg = 'gray93')
    if str(per[name][8]) == "0":
        btntwon.configure(bg = "red",fg = "white")
        btntwoy.configure(fg = "black",bg = 'gray93')
    else:
        btntwoy.configure(bg = "red",fg = "white")
        btntwon.configure(fg = "black",bg = 'gray93')
    if str(per[name][9]) == "0":
        btnbign.configure(bg = "red",fg = "white")
        btnbigy.configure(fg = "black",bg = 'gray93')
    else:
        btnbigy.configure(bg = "red",fg = "white")
        btnbign.configure(fg = "black",bg = 'gray93')
    ennatxt.set(per[name][0])
    entimetxt.set(per[name][3])
    enrighttxt.set(per[name][6])   
    for i in range(0,5):
        if daym[i]!="0":
            permo[i] = 1
        else:
            permo[i] = 0
    for i in range(0,5):
        if daya[i]!="0":
            peraf[i] = 1
        else:
            peraf[i] = 0
    if per[name][4] == "0":
        persen[0] = 0
    else:
        persen[0] = 1
    if per[name][5] == "0":
        perright[0] = 0
    else:
        perright[0] = 1
    if per[name][7] == "0":
        perback[0] = 0
    else:
        perback[0] = 1
    if per[name][8] == "0":
        pertwo[0] = 0
    else:
        pertwo[0] = 1
    if per[name][9] == "0":
        perbig[0] = 0
    else:
        perbig[0] = 1
    btmbtntxt.set("修改")
    adedchange = 0
def add():
    global adedchange
    btmbtntxt.set("新增")
    selected_item = tree.get_children() ## get selected item
    tree.delete(selected_item)
    addlist = [btnm1,btntu1,btnw1,btnth1,btnf1,btnm2,btntu2,btnw2,btnth2,btnf2]
    ennatxt.set("")
    for i in range(len(addlist)):
        addlist[i].configure(fg = "black",bg = 'gray93')
    enrighttxt.set("")
    entimetxt.set("")
    btnsenn.configure(fg = "black",bg = 'gray93')
    btnseny.configure(fg = "black",bg = 'gray93')
    btnrightn.configure(fg = "black",bg = 'gray93')
    btnrighty.configure(fg = "black",bg = 'gray93')
    btntwoy.configure(fg = "black",bg = 'gray93')
    btntwon.configure(fg = "black",bg = 'gray93')
    btnbackn.configure(fg = "black",bg = 'gray93')
    btnbacky.configure(fg = "black",bg = 'gray93')
    btnbign.configure(fg = "black",bg = 'gray93')
    btnbigy.configure(fg = "black",bg = 'gray93')
    adedchange = 1



main = tk.Tk()
main.geometry("1000x600")
main.title("基礎設定")

c = [0,0,0,0,0,0,0,0,0,0]

ptxt = open("edit.txt","r",encoding="utf-8")
line = len(ptxt.readlines())
per = [[0] *10 for i in range(line)]
peredit = [0,0,0,0,0,0,0,0,0,0]
permo = [5,5,5,5,5]
peraf = [5,5,5,5,5]
persen = [5]
perright = [5]
perback = [5]
pertwo = [5]
perbig = [5]
adedchange = 0
name = line-1
ptxt = open("edit.txt","r",encoding="utf-8")
for i in range(line):
    f = ptxt.readline()
    per[i] = list(f.split())
#listbox
listbox = tk.Listbox(main,font = ("新細明體",20), width = 7)
for i in range(line):
    listbox.insert(END,per[i][0])
listbox.pack(side = "left",fill = "y")
#label
pd = tk.StringVar()
pd.set("請選取要更改的人")
peda = tk.Label(main,textvariable = pd,font = ("新細明體",30))
peda.pack()

#tree-data
style = ttk.Style(main)
style.configure('Calendar.Treeview', rowheight=30,font = ("新細明體",20),stretch = False)
tree=ttk.Treeview(main,style = 'Calendar.Treeview',show='headings',height = 1)
tree["columns"]=("名字","上午","下午","值勤天數","學長姐","正打","正打次數","二燈","大燈")
tree.column("名字",width=90,anchor='center')
tree.column("上午",width=150,anchor='center')
tree.column("下午",width=150,anchor='center')
tree.column("值勤天數",width=100,anchor='center')
tree.column("學長姐",width=60,anchor='center')
tree.column("正打",width=80,anchor='center')
tree.column("正打次數",width=80,anchor='center')
tree.column("二燈",width=80,anchor='center')
tree.column("大燈",width=80,anchor='center')

tree.heading("名字",text="名字")
tree.heading("上午",text="上午")  #顯示表頭
tree.heading("下午",text="下午")
tree.heading("值勤天數",text="值勤天數")
tree.heading("學長姐",text="學長姐")
tree.heading("正打",text="正打")
tree.heading("正打次數",text="正打次數")
tree.heading("二燈",text="二燈")
tree.heading("大燈",text="大燈")
tree.pack()
tree.insert("",0,text="資料" ,values=("none"))
#button-choose
chtxt = tk.StringVar()
chtxt.set("選擇")
ch = tk.Button(main,textvariable = chtxt,command = choose,font = ("新細明體",10))
ch.pack(anchor = "sw")
#button-add
ad = tk.Button(main,text = "新增",command = add,font = ("新細明體",10),fg = "red")
ad.pack(anchor = "sw")

#label-name
lana = tk.Label(main,text = "名字",font = ("新細明體",20))
lana.pack(anchor = "sw")
#label-morning
lamo = tk.Label(main,text = "上午班次",font = ("新細明體",20))
lamo.pack(anchor = "sw")
#label-afternoon
laaf = tk.Label(main,text = "下午班次",font = ("新細明體",20))
laaf.pack(anchor = "sw")
#label-day
lada = tk.Label(main,text = "值勤幾次",font = ("新細明體",20))
lada.pack(anchor = "sw")
#label-senbi
lase = tk.Label(main,text = "學長姐(不值大檔魯班)",font = ("新細明體",20))
lase.pack(anchor = "sw")
#label-right
lari = tk.Label(main,text = "正打",font = ("新細明體",20))
lari.pack(anchor = "sw")
#label-right time
lariti = tk.Label(main,text = "正打次數",font = ("新細明體",20))
lariti.pack(anchor = "sw")
#label-back
laba = tk.Label(main,text = "撤哨",font = ("新細明體",20))
laba.pack(anchor = "sw")
#label-two
latw = tk.Label(main,text = "二燈",font = ("新細明體",20))
latw.pack(anchor = "sw")
#label-big
labi = tk.Label(main,text = "大燈",font = ("新細明體",20))
labi.pack(anchor = "sw")
#entry-name
ennatxt = tk.StringVar()
enna = tk.Entry(main,textvariable = ennatxt)
enna.place(x=520,y=158)
#button-morning
txtmo = [0,0,0,0,0]
day = ["一","二","三","四","五"]
for i in range(0,5):
    txtmo[i] = tk.StringVar()
    txtmo[i].set(str(day[i]))
btnm1 = tk.Button(main,textvariable = txtmo[0],command = partial(change_label_numer,0),font = ("新細明體",15))
btntu1 = tk.Button(main,textvariable = txtmo[1],command = partial(change_label_numer,1),font = ("新細明體",15))
btnw1 = tk.Button(main,textvariable = txtmo[2],command = partial(change_label_numer,2),font = ("新細明體",15))
btnth1 = tk.Button(main,textvariable = txtmo[3],command = partial(change_label_numer,3),font = ("新細明體",15))
btnf1 = tk.Button(main,textvariable = txtmo[4],command = partial(change_label_numer,4),font = ("新細明體",15))
btnm1.place(x=520,y=185)
btntu1.place(x=560,y=185)
btnw1.place(x=600,y=185)
btnth1.place(x=640,y=185)
btnf1.place(x=680,y=185)
#-----
txtaf = [0,0,0,0,0]
for i in range(0,5):
    txtaf[i] = tk.StringVar()
    txtaf[i].set(str(day[i]))
btnm2 = tk.Button(main,textvariable = txtaf[0],command = partial(change_label_numer,5),font = ("新細明體",15))
btntu2 = tk.Button(main,textvariable = txtaf[1],command = partial(change_label_numer,6),font = ("新細明體",15))
btnw2 = tk.Button(main,textvariable = txtaf[2],command = partial(change_label_numer,7),font = ("新細明體",15))
btnth2 = tk.Button(main,textvariable = txtaf[3],command = partial(change_label_numer,8),font = ("新細明體",15))
btnf2 = tk.Button(main,textvariable = txtaf[4],command = partial(change_label_numer,9),font = ("新細明體",15))
btnm2.place(x=520,y=215)
btntu2.place(x=560,y=215)
btnw2.place(x=600,y=215)
btnth2.place(x=640,y=215)
btnf2.place(x=680,y=215)
#entry-times
entimetxt = tk.StringVar()
entime = tk.Entry(main,textvariable = entimetxt)
entime.place(x=520,y=255)
#button-senbi
btnseny = tk.Button(main,text = "不值",command = partial(change_label_numer,11),font = ("新細明體",15))
btnsenn = tk.Button(main,text = "值",command = partial(change_label_numer,10),font = ("新細明體",15))
btnseny.place(x=520,y=278)
btnsenn.place(x=580,y=278)
#button-right
btnrighty = tk.Button(main,text = "是",command = partial(change_label_numer,12),font = ("新細明體",15))
btnrightn = tk.Button(main,text = "否",command = partial(change_label_numer,13),font = ("新細明體",15))
btnrighty.place(x=520,y=316)
btnrightn.place(x=560,y=316)
#entry-right times
enrighttxt = tk.StringVar()
enright = tk.Entry(main,textvariable = enrighttxt)
enright.place(x=520,y=355)
#button-back
btnbacky = tk.Button(main,text = "是",command = partial(change_label_numer,18),font = ("新細明體",15))
btnbackn = tk.Button(main,text = "否",command = partial(change_label_numer,19),font = ("新細明體",15))
btnbacky.place(x=520,y=375)
btnbackn.place(x=560,y=375)
#button-two
btntwoy = tk.Button(main,text = "是",command = partial(change_label_numer,14),font = ("新細明體",15))
btntwon = tk.Button(main,text = "否",command = partial(change_label_numer,15),font = ("新細明體",15))
btntwoy.place(x=520,y=415)
btntwon.place(x=560,y=415)
#button-big
btnbigy = tk.Button(main,text = "是",command = partial(change_label_numer,16),font = ("新細明體",15))
btnbign = tk.Button(main,text = "否",command = partial(change_label_numer,17),font = ("新細明體",15))
btnbigy.place(x=520,y=455)
btnbign.place(x=560,y=455)

#button-delete
edit = tk.Button(main,text = "刪除",command = delete ,font = ("新細明體",10),fg = "red")
edit.pack(anchor = "sw")

#button-edit
btmbtntxt = tk.StringVar()
edit = tk.Button(main,textvariable = btmbtntxt,command = lastedit ,font = ("新細明體",10),fg = "red")
edit.pack(side = "bottom")
btmbtntxt.set("修改")

main.mainloop()
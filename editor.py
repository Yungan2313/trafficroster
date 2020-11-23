import tkinter as tk
from tkinter import END
from tkinter import Y
from  tkinter import ttk
from tkinter import Grid
from functools import partial


def lastedit():
    a = 0
def change_label_numer(dd):
    if dd<10:
        a = [btnm1,btntu1,btnw1,btnth1,btnf1,btnm2,btntu2,btnw2,btnth2,btnf2]
        b = a[dd]
        if c[dd] == 0:
            b.configure(bg = "red",fg = "white")
            c[dd] = 1
        else:
            b.configure(fg = "black",bg = 'gray93')
            c[dd] = 0
    else:
        
def choose():
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
    ennatxt.set(per[name][0])
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
    entimetxt.set(per[name][3])
def add():
    a = 0
    

main = tk.Tk()
main.geometry("1000x600")
main.title("基礎設定")

c = [0,0,0,0,0,0,0,0,0,0]

ptxt = open("p.txt","r",encoding="utf-8")
line = len(ptxt.readlines())
per = [[0] *10 for i in range(line)]
ptxt = open("p.txt","r",encoding="utf-8")
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
# #name
# lantxt = tk.StringVar()
# lan = tk.Label(main,textvariable = lantxt)
# lan.pack()
# #morning
# lamtxt = tk.StringVar()
# lam = tk.Label(main,dafr,textvariable = lamtxt)
# lam.grid(row = 0,column = 1)
# #afternoon
# laatxt = tk.StringVar()
# laa = tk.Label(main,dafr,textvariable = laatxt)
# laa.grid(row = 0,column = 2)
# #day
# ladtxt = tk.StringVar()
# lad = tk.Label(main,dafr,textvariable = ladtxt)
# lad.grid(row = 0,column = 3)
# #senby
# lastxt = tk.StringVar()
# las = tk.Label(main,dafr,textvariable = lastxt)
# las.grid(row = 0,column = 4)
# #right
# lartxt = tk.StringVar()
# lar = tk.Label(main,dafr,textvariable = lartxt)
# lar.grid(row = 0,column = 5)
# #right time
# larttxt = tk.StringVar()
# lart = tk.Label(main,dafr,textvariable = larttxt)
# lart.grid(row = 0,column = 6)
# #fell back
# laftxt = tk.StringVar()
# laf = tk.Label(main,dafr,textvariable = laftxt)
# laf.grid(row = 0,column = 7)
# #two
# lattxt = tk.StringVar()
# lat = tk.Label(main,dafr,textvariable = lattxt)
# lat.grid(row = 0,column = 8)
# #big
# labtxt = tk.StringVar()
# lab = tk.Label(main,dafr,textvariable = labtxt)
# lab.grid(row = 0,column = 8)

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
btnm1.place(x=520,y=180)
btntu1.place(x=560,y=180)
btnw1.place(x=600,y=180)
btnth1.place(x=640,y=180)
btnf1.place(x=680,y=180)
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
btnm2.place(x=520,y=210)
btntu2.place(x=560,y=210)
btnw2.place(x=600,y=210)
btnth2.place(x=640,y=210)
btnf2.place(x=680,y=210)
#entry-times
entimetxt = tk.StringVar()
entime = tk.Entry(main,textvariable = entimetxt)
entime.place(x=520,y=255)
#button-senbi
butsen = tk.Button(main,text = "是",command = no)

#button-edit
edit = tk.Button(main,text = "修改",command = lastedit ,font = ("新細明體",10),fg = "red")
edit.pack(side = "bottom")

main.mainloop()
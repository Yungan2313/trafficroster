import tkinter as tk
from tkinter import END
from tkinter import Y
from  tkinter import ttk
from tkinter import Grid

def choose():
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
    if per[name][5] == 1:
        senbi = "是"
    else:
        senbi = "否"
    tree.insert("",0,text="資料" ,values=("{0}".format(per[name][0]),"{0}".format(daymtxt),"{0}".format(dayatxt),"{0}".format(per[name][3]),"{0}".format(senbi),"{0}".format(per[name][5]),"{0}".format(per[name][6]),"{0}".format(per[name][7]),"{0}".format(per[name][8])))
def add():
    a = 0
    

main = tk.Tk()
main.geometry("1000x600")
main.title("基礎設定")

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

#button-edit
edit = tk.Button(main,text = "修改",command = add,font = ("新細明體",10),fg = "red")
edit.pack(side = "bottom")

main.mainloop()
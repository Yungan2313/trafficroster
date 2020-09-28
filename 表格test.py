import tkinter
from  tkinter import ttk  #导入内部包
 
win=tkinter.Tk()
tree=ttk.Treeview(win)#表格
tree["columns"]=("魯班","大檔","北管","二打","正打","打三","二燈","大燈")
#表示列,不显示
tree.column("魯班",width=100)
tree.column("大檔",width=100)
tree.column("北管",width=100)
tree.column("二打",width=100)
tree.column("正打",width=100)
tree.column("打三",width=50)
tree.column("二燈",width=50)
tree.column("大燈",width=50)

tree.heading("魯班",text="魯班")  #显示表头
tree.heading("大檔",text="大檔")
tree.heading("北管",text="北管")
tree.heading("二打",text="二打")
tree.heading("正打",text="正打")
tree.heading("打三",text="打三")
tree.heading("二燈",text="二燈")
tree.heading("大燈",text="大燈")

a = "fuck"

tree.insert("",0,text="星期一上午" ,values=("{0}  {1}".format(a,a),"{0}".format(a),"{0}".format(a),"{0}".format(a),"{0}".format(a),"{0}".format(a),"{0}".format(a),"{0}".format(a))) #插入数据，
tree.insert("",1,text="星期一下午" ,values=("{0}".format(a),"{0}".format(a),"{0}".format(a),"{0}".format(a),"{0}".format(a),"{0}".format(a),"{0}".format(a),"{0}".format(a)))
tree.insert("",2,text="星期二上午" ,values=("{0}".format(a),"{0}".format(a),"{0}".format(a),"{0}".format(a),"{0}".format(a),"{0}".format(a),"{0}".format(a),"{0}".format(a)))
tree.insert("",3,text="星期二下午" ,values=("{0}".format(a),"{0}".format(a),"{0}".format(a),"{0}".format(a),"{0}".format(a),"{0}".format(a),"{0}".format(a),"{0}".format(a)))
tree.insert("",4,text="星期三上午" ,values=("{0}".format(a),"{0}".format(a),"{0}".format(a),"{0}".format(a),"{0}".format(a),"{0}".format(a),"{0}".format(a),"{0}".format(a)))
tree.insert("",5,text="星期三下午" ,values=("{0}".format(a),"{0}".format(a),"{0}".format(a),"{0}".format(a),"{0}".format(a),"{0}".format(a),"{0}".format(a),"{0}".format(a)))
tree.insert("",6,text="星期四上午" ,values=("{0}".format(a),"{0}".format(a),"{0}".format(a),"{0}".format(a),"{0}".format(a),"{0}".format(a),"{0}".format(a),"{0}".format(a)))
tree.insert("",7,text="星期四下午" ,values=("{0}".format(a),"{0}".format(a),"{0}".format(a),"{0}".format(a),"{0}".format(a),"{0}".format(a),"{0}".format(a),"{0}".format(a)))
tree.insert("",8,text="星期五上午" ,values=("{0}".format(a),"{0}".format(a),"{0}".format(a),"{0}".format(a),"{0}".format(a),"{0}".format(a),"{0}".format(a),"{0}".format(a)))
tree.insert("",9,text="星期五下午" ,values=("{0}".format(a),"{0}".format(a),"{0}".format(a),"{0}".format(a),"{0}".format(a),"{0}".format(a),"{0}".format(a),"{0}".format(a)))
 
tree.pack()
win.mainloop()

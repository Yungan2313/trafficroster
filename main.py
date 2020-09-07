import re
ptxt = open("p.txt","r",encoding="utf-8")
per = [[0] *10 for i in range(2)]
line = len(ptxt.readlines())
ptxt = open("p.txt","r",encoding="utf-8")
for i in range(line):
    f = ptxt.readline()
    per[i] = list(f.split())
print(per[1][1])
import re
ptxt = open("p.txt","r",encoding="utf-8")
f = []
line = len(ptxt.readlines())
ptxt = open("p.txt","r",encoding="utf-8")
for i in range(line):
    f.append(ptxt.readline())
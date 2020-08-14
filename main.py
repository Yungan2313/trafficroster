import re
ptxt = open("p.txt","r",encoding="utf-8")
f = []
# line = len(ptxt.readlines())

f.append(ptxt.readline())
f.append(ptxt.readline())
print(f[0],f[1],sep="\n")
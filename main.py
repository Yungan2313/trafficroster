import re
ptxt = open("p.txt","r",encoding="utf-8")
f = []
f.append(ptxt.readline())
f.append(ptxt.readline())
print(f[0],f[1],sep="\n")
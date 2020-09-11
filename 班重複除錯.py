a = "1,2,3,4,5"
b = []
for i in range (0,5):
    b = list(a.split(","))
    b[0] = "0"
    a = b
import random
lists = [12, 23, 13, 14, 78, 234, 123, 12345]
i = []
i = lists
layer = []
for i in range(0,10):
    layer.append(i)
random.shuffle(layer)
print(layer)
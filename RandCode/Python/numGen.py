import random

def getTemp():
    list = []
    num = 0
    for i in range(0, 12):
        num = random.uniform(0, 10)
        numForm = "%.1f" % num
        list.append(numForm)
    return list

for i in range(0, 3):
    print(getTemp())

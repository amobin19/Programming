# amobin19 07/11/2018

import webbrowser
import random
import sys

url = 'www.google.com'

webbrowser.open_new_tab(url)

webbrowser.open_new(url)

foo = "foo"
bar = "bar"
foobar = foo + bar
print(foobar)

list1 = ["a", "b"]
numList = []

s = ""
for i in list1:
    s+=i
    print(s)

for num in range(1, sys.maxsize):
    numList.append(num)
    print(numList)

value = random.randint(1, sys.maxsize)
print(value)

print(float("inf") > sys.maxsize)
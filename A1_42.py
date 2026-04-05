import math
command = input()
x = 0
y = 0

for i in command:
    if i == "N":
        y += 1
    elif i == "S":
        y -= 1
    elif i == "E":
        x += 1
    elif i == "W":
        x -= 1

print(x, y, abs(x+y))
import random
import math

def chance(n):
    x=random.random()*16
    if x<1:n=(n-3)%40
    elif x<2:n=0
    elif x<3:n=11
    elif x<5:
        n-=5
        n/=10
        n=math.ceil(n)*10
        n=(n+5)%40
    elif x<6:n=39
    elif x<7:n=10
    elif x<8:n=24
    elif x<9:n=5
    elif x<10:
        if n<28 and n>12:n=28
        else:n=12
    else:n=(n+diceRoll())%40
    return n

def commChest(n):
    x=random.random()*16
    if x<1:n=10
    elif x<2:n=0
    else:n=(n+diceRoll())%40
    return n

def diceRoll():
    return math.floor(random.random()*6+random.random()*6)

pos = 0
landed = [0]*40
repeat = 3000
turns = 20
for j in [0]*repeat:
    for i in [0]*turns:
        if pos in [7,22,36]:
            pos = chance(pos)
        elif pos in [2,17,32]:
            pos = commChest(pos)
        elif pos==30:pos=10
        else:pos=(pos+diceRoll())%40
        landed[pos]=landed[pos]+1
print(landed)

with open("runs.csv","a") as file:
    file.write(str(repeat)+","+str(turns)+","+",".join(str(i/(repeat*turns))for i in landed)+"\n")

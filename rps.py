from random import randint
import re

#w,l
g = False
t = [["r", "s"], ["p", "r"], ["s", "p"]]

while g == False :
    c = t[randint(0,2)]
    p = input("rock, paper or scissors?")

    if re.match("^[rps]$", p) == None :
        print("Wrong input")
        continue

    if c[1] == p :
        g = True
        print("Win")
    elif c[0] == p : 
        print("Draw")
        continue
    else :
        g = True
        print("Lose")

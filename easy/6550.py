# %%
import sys

sys.stdin = open("input.txt", "r")

while line := sys.stdin.readline():
    s , t = line.split()

    for i in t:
        if s and s[0] == i:
            s = s[1:]
    
    if s:
        print("No")
    else:
        print("Yes")
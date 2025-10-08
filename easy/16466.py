# %%
import sys

sys.stdin = open("input.txt", "r")

N = int(sys.stdin.readline())

A = { k : 1  for k in list(map(int, sys.stdin.readline().split()))}

for i in range(1,2**31):
    if i not in A:
        print(i)
        break

# %%

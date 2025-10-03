# %%
import sys

sys.stdin = open("input.txt", "r")

N, T = map(int, sys.stdin.readline().split())

arms = 1
add_num = 1
for _ in range(T-1):
    arms += add_num
    if arms == 2*N:
        add_num = -1
    if arms == 1:
        add_num = +1

print(arms)


# %%

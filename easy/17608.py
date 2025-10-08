# %%
import sys

sys.stdin = open("input.txt", "r")

N = int(sys.stdin.readline())

bars = [int(sys.stdin.readline()) for _ in range(N)]

cnt, largest = 0, -1
for i in range(N-1,-1,-1):
    if bars[i] > largest:
        largest= bars[i]
        cnt +=1

print(cnt)
# %%

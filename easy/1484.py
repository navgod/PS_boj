# %%
import sys

sys.stdin = open("input.txt", "r")

N = int(sys.stdin.readline())
ans = []
for i in range(1,100000):
    min = int((i**2 - 100_000)**0.5) if i**2 > 100_000 else 1
    for j in range(min,i):
        if i**2 -j**2 == N:
            ans.append(i)
if len(ans) ==0:
    print(-1)
else:
    for a in ans:
        print(a)
# %%

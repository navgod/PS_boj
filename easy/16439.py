# %%
import sys
from itertools import combinations
sys.stdin = open("input.txt", "r")

N, M = map(int , sys.stdin.readline().split())
favor = [list(map(int , sys.stdin.readline().split())) for _ in range(N)]
ans = -1
for comb in combinations(list(range(M)),3):
    residual = 0
    for i in range(N):
        satifaction = 0
        for c in comb:
            satifaction = max(satifaction, favor[i][c])
        residual += satifaction
    ans = max(ans, residual)
print(ans)

# %%

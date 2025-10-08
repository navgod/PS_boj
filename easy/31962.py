# %%
import sys

sys.stdin = open("input.txt", "r")

N, X = map(int, sys.stdin.readline().split())

ans = float('-inf')

for _ in range(N):
    S, T = map(int, sys.stdin.readline().split())
    if S+T <=X:
        ans = max(ans, S)

print(ans if ans >0 else -1)
# %%

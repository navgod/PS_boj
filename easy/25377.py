# %%
import sys

sys.stdin = open("input.txt", "r")

N = int(sys.stdin.readline())
ans = float('inf')
for _ in range(N):
    distance, arrive = map(int, sys.stdin.readline().split())
    if distance <= arrive:
        ans = min(ans,arrive)

print(-1 if ans > 1000 else ans)
# %%

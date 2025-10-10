# %%
import sys

sys.stdin = open("input.txt", "r") 

N = int(sys.stdin.readline())
costs = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

## RGB 순 2차원 dp
dp = [[float('inf')]*3 for _ in range(N)]

for i in range(3):
    dp[0][i] = costs[0][i]

for i in range(1,N):
    dp[i][0] = min(dp[i-1][1],dp[i-1][2])+costs[i][0]
    dp[i][1] = min(dp[i-1][0],dp[i-1][2])+costs[i][1]
    dp[i][2] = min(dp[i-1][1],dp[i-1][0])+costs[i][2]

print(min(dp[-1]))
# %%

# %%
import sys

sys.stdin = open("input.txt", "r")

N = int(sys.stdin.readline())

dp = [[0]*N for _ in range(N)]
tree = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]

dp[0][0] = tree[0][0]

for i in range(1,N):
    for j in range(i+1):
        dp[i][j] = dp[i-1][j]
        if j >0:
            dp[i][j] = max(dp[i][j], dp[i-1][j-1])
        dp[i][j] += tree[i][j]

print(max(dp[-1]))
# %%

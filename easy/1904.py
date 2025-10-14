# %%
import sys

sys.stdin = open("input.txt", "r")
mod= 15746
N = int(sys.stdin.readline())
dp = [0] * (1_000_001)
dp[1] = 1
dp[2] = 2
for i in range(3,N+1):
    dp[i] = (dp[i-1] + dp[i-2]) % mod

print(dp[N])


# %%

# %%
import sys

sys.stdin = open("input.txt", "r")

n, k = map(int, sys.stdin.readline().split())

dp = [0]* (k+1) 
value = [int(sys.stdin.readline()) for _ in range(n)]
dp[0] = 1

for v in value:
    for i in range(v, k+1):
        dp[i] += dp[i-v]

    
print(dp[k])

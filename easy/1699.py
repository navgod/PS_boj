# %%
import sys
from itertools import combinations

sys.stdin = open("input.txt", "r") 

N = int(sys.stdin.readline())

dp = [0] * (N+1)

for i in range(1,N+1):
    if (i**0.5).is_integer():
        dp[i] = 1
        continue

    dp[i] = float('inf')
    j = 1
    while j** 2 <= i:
        dp[i] = min(dp[i], dp[i-j**2] + 1)
        j +=1

print(dp[N])
# %%

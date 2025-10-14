# %%
import sys

sys.stdin = open("input.txt", "r")

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
# dp[i] 는 i를 마지막으로 하는 가장 긴 증가하는 부분수열
dp = [1]*N

for i in range(1,N):
    for j in range(0,i):
        if A[i] > A[j]:
            dp[i] = max(dp[i],dp[j]+1)


print(max(dp))

# %%

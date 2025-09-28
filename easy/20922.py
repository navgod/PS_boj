# %%
import sys

sys.stdin = open("input.txt", "r")
N, K = map(int, sys.stdin.readline().split())
A = list(map(int, sys.stdin.readline().split()))

ans = -1

count = [0] * 100_001

start = 0
for end in range(N):
    count[A[end]] += 1
    
    while count[A[end]] > K:
        count[A[start]] -= 1
        start += 1
        
    ans = max(ans, end - start + 1)
    
print(ans)
# %%

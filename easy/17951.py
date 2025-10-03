# %%
import sys
sys.stdin = open("input.txt", "r")

N, K = map(int, sys.stdin.readline().split())
A = list(map(int, sys.stdin.readline().split()))
low = 0
high = 20 * 10**5
ans = 0
while low <= high:
    mid = (low + high) //2

    cnt = 0
    residual = 0
    for i in range(N):
        residual += A[i]
        if residual >= mid:
            residual = 0
            cnt += 1
    if cnt >= K:
        ans = mid
        low = mid + 1
    else:
        high = mid -1
print(ans)

# %%

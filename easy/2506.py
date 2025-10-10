# %%
import sys

sys.stdin = open("input.txt", "r") 

N = int(sys.stdin.readline())
A = list(map(int , sys.stdin.readline().split()))

cnt = 0
ans = 0
for i in range(N):
    if A[i] == 1:
        ans += cnt +1
        cnt += 1
    else:
        cnt = 0
print(ans)
# %%

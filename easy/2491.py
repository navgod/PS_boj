# %%
import sys

sys.stdin = open("input.txt", "r") 

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))

longest = -1
cnt = 0
for i in range(N):
    if i == 0 or A[i-1] <= A[i]:
        cnt += 1
    else:
        cnt = 1
    longest = max(longest, cnt)
cnt = 0
for i in range(N):
    if i == 0 or A[i-1] >= A[i]:
        cnt += 1
    else:
        cnt = 1
    longest = max(longest, cnt)
print(longest)
# %%

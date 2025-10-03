# %%
import sys
sys.stdin = open("input.txt", "r")

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
B = [0]* N
B[0] = A[0]
for i in range(1,N):
    B[i] = B[i-1]+ A[i]
ans = -1
for i in range(1,N-1):
    road1, road2 = B[i-1]-B[0] , B[N-2] - B[i]
    ans = max(
        ans,
        2*road1 + road2 + 2*A[0],
        road1 + road2 + 2*A[i],
        road1 + 2*road2 + 2*A[N-1]
    )
print(ans)

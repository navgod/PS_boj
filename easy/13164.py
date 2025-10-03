# %%
import sys

sys.stdin = open("input.txt", "r")

N, K = map(int, sys.stdin.readline().split())
A = list(map(int, sys.stdin.readline().split()))

D = [A[i]-A[i-1] for i in range(1,N)]

D.sort(reverse=True)

total = A[N-1]- A[0]

for i in range(K-1):
    total -= D[i]

print(total)
# %%

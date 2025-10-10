# %%
import sys

sys.stdin = open("input.txt", "r") 

N = int(sys.stdin.readline())
A = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

ranks = []

for i in range(N):
    rank = 1
    for j in range(N):
        if i != j:
            if A[j][0] > A[i][0] and A[j][1] > A[i][1]:
                rank += 1
    ranks.append(rank)

print(*ranks)
# %%

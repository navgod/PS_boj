# %%
import sys

sys.stdin = open("input.txt",  "r")

N, P, Q = map(int ,sys.stdin.readline().split())
A = list( map(int ,sys.stdin.readline().split()))
B = list( map(int ,sys.stdin.readline().split()))
if P == Q:
    n = []
    for i in range(N):
        if B[i] == A[i]:
            n.append(0)
    if len(n) == N:
        print("YES")
        for i in range(N):
            print(n[i], end=" ")
    else:
        print("NO")
else:
    n = []
    for i in range(N):
        cand , resi = (B[i]-A[i])//(P-Q) , (B[i]-A[i])%(P-Q)
        if resi == 0 and cand >= 0:
            n.append(cand)
    
    if len(n) == N:
        print("YES")
        for i in range(N):
            print(n[i], end=" ")
    else:
        print("NO")

# %%

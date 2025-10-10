# %%
import sys

sys.stdin = open("input.txt", "r") 

N, M = map(int , sys.stdin.readline().split())

for _ in range(N):
    A = sys.stdin.readline().strip()
    print(A[::-1])
# %%

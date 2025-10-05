# %%
import sys
from collections import Counter
sys.stdin = open("input.txt",  "r")

N = int(sys.stdin.readline())
A = Counter(map(int,sys.stdin.readline().split()))
B = Counter(map(int,sys.stdin.readline().split()))

for a in A:
    if a in B:
        min_num = min(A[a],B[a])
        A[a] -= min_num
        B[a] -= min_num
print(sum([v for k, v in A.items()]))
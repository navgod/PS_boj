# %%
import sys
from itertools import combinations
sys.stdin = open("input.txt", "r")

A = []
for i in range(1,11):
    for combination in combinations(list(range(10)),i):
        number = 0
        for n in combination[::-1]:
            number *= 10
            number += n
        A.append(number)

A.sort()

N = int(sys.stdin.readline())
if N < len(A):
    print(A[N])
else:
    print(-1)
# %%

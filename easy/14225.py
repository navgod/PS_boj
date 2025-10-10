# %%
import sys
from itertools import combinations
sys.stdin = open("input.txt", "r") 

N = int(sys.stdin.readline())
S = list(map(int, sys.stdin.readline().split()))
all_set = set()

for i in range(N+1):
    for comb in combinations(S,i):
        all_set.add(sum(comb))

for i in range(1,10**7):
    if i not in all_set:
        print(i)
        break

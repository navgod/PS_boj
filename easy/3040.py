# %%
import sys
from itertools import combinations

sys.stdin = open("input.txt", "r") 

nums = [int(sys.stdin.readline()) for _ in range(9)]

for comb in combinations(nums, 7):
    if sum(comb) == 100:
        for i in range(7):
            print(comb[i])
        break
# %%

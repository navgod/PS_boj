# %%
import sys
from itertools import combinations

sys.stdin = open("input.txt", "r") 

N, M = map(int, sys.stdin.readline().split())
house = []
chicken = []

for i in range(N):
    line = list(map(int, sys.stdin.readline().split()))
    for j in range(N):
        if line[j] == 1:
            house.append((i,j))
        elif line[j] == 2:
            chicken.append((i,j))
    
min_dist = float('inf')

for comb in combinations(chicken, M):
    dist = 0
    for x,y in house:
        house_dist = float('inf')
        for u, v in comb:
            house_dist = min(house_dist, abs(u-x) + abs(v-y))
        dist += house_dist
    min_dist= min(min_dist, dist)

print(min_dist)
# %%

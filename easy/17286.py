# %%
import sys
from itertools import permutations

sys.stdin = open("input.txt", "r")

points = [list(map(int, sys.stdin.readline().split())) for _ in range(4)]

distance = [[0]*4 for _ in range(4)]

for i in range(4):
    for j in range(4):
        distance[i][j] = ((points[i][0]-points[j][0])**2 + (points[i][1]- points[j][1])**2 )**0.5

min_distance= float('inf') 

for perm in permutations(range(1,4),3):
    now_distance = distance[0][perm[0]]
    for i in range(1,3):
        now_distance += distance[perm[i-1]][perm[i]]
    min_distance = min(min_distance, int(now_distance))
print(min_distance)
# %%

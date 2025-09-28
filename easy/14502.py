# %%
from collections import deque
from itertools import combinations
import copy
import sys

sys.stdin = open("input.txt" , 'r')

dxs , dys = [1, -1, 0, 0] , [0, 0, 1, -1]

def cal_area(lab):
    global r,c
    area = 0
    for i in range(r):
        for j in range(c):
            if lab[i][j] == 0:
                area += 1
    return area

def bfs(lab,virus):
    Q = deque(virus)
    copy_lab = copy.deepcopy(lab)
    while(Q):
        r, c = Q.popleft()
        for dx, dy in zip(dxs,dys):
            nr, nc = r + dx , c + dy
            if 0 <= nr < len(lab) and 0 <= nc < len(lab[0]) and copy_lab[nr][nc] == 0:
                copy_lab[nr][nc] = 2
                Q.append((nr,nc))
    return cal_area(copy_lab)

r, c = map(int , sys.stdin.readline().split())

virus = []
empty = []
lab = []
for i in range(r):
    line = list(map(int, sys.stdin.readline().split()))
    lab.append(line)
    for j in range(c):
        if line[j] == 2:
            virus.append((i,j))
        elif line[j] == 0:
            empty.append((i,j))

ans = -1

for comb in combinations(empty,3):
    for i, j in comb:
        lab[i][j] = 1
    ans = max(ans, bfs(lab,virus))
    for i, j in comb:
        lab[i][j] = 0

print(ans)
# %%

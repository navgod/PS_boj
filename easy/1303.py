# %%
import sys
from collections import deque

sys.stdin = open("input.txt", "r")

c, r = map(int, sys.stdin.readline().split())

visited = [[False]*c for _ in range(r)]

grid = [list(sys.stdin.readline().rstrip()) for _ in range(r)]

Q = deque()
dxs, dys = [1,-1,0,0] , [0,0,1,-1]
power = {
    'W' : 0,
    'B' : 0
}
for i in range(r):
    for j in range(c):
        if not visited[i][j]:
            visited[i][j] = True
            cnt = 1
            Q.append((i,j,grid[i][j]))
            while Q:
                row, col, color = Q.popleft()
                for dx, dy in zip(dxs, dys):
                    nr , nc = row + dx, col + dy
                    if 0<= nr < r and 0 <= nc < c and not visited[nr][nc] and grid[nr][nc] == color:
                        visited[nr][nc] = True
                        Q.append((nr,nc,color))
                        cnt += 1
            power[color] += cnt**2

print(power['W'],power['B'])
# %% 두번째 풀이
import sys

sys.stdin = open("input.txt", "r")

C, R = map(int, sys.stdin.readline().split())
grid = [list(sys.stdin.readline().rstrip()) for _ in range(R)]

parent = [i for i in range(R * C)]
size = [1] * (R * C)

def find(x):
    if parent[x] == x:
        return x
    parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    rootX = find(x)
    rootY = find(y)

    if rootX != rootY:
        if size[rootX] < size[rootY]:
            rootX, rootY = rootY, rootX # rootX가 항상 더 큰 쪽이 되도록
        
        parent[rootY] = rootX
        size[rootX] += size[rootY]

for r in range(R):
    for c in range(C):
        idx = r * C + c
        if c + 1 < C and grid[r][c] == grid[r][c + 1]:
            union(idx, idx + 1)
        if r + 1 < R and grid[r][c] == grid[r + 1][c]:
            union(idx, idx + C)

power = {'W': 0, 'B': 0}
processed_roots = set() 

for r in range(R):
    for c in range(C):
        idx = r * C + c
        root = find(idx)
        
        if root not in processed_roots:
            group_size = size[root]
            color = grid[r][c]
            power[color] += group_size ** 2
            processed_roots.add(root)

print(power['W'], power['B'])
# %%

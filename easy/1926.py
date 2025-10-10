# %%
import sys
from collections import deque

sys.stdin = open("input.txt", "r") 

n, m = map(int, sys.stdin.readline().split())

drawing = [list( map(int, sys.stdin.readline().split())) for _ in range(n)]

Q = deque()

visited = [[False]*m for _ in range(n)]

dxs, dys = [1,-1,0,0] , [0,0,1,-1]
cnt, area = 0, 0
max_area = 0

for r in range(n):
    for c in range(m):
        if drawing[r][c] == 1 and not visited[r][c]:
            visited[r][c] = True
            cnt += 1
            area += 1
            Q.append((r,c))
            while Q:
                row,col = Q.popleft()
                for dx, dy in zip(dxs,dys):
                    nx, ny = row + dx , col + dy
                    if 0 <= nx < n and 0<= ny < m and not visited[nx][ny] and drawing[nx][ny] == 1:
                        area += 1
                        visited[nx][ny] = True
                        Q.append((nx,ny))
            max_area = max(max_area, area)
            area = 0
print(cnt)
print(max_area)
# %%

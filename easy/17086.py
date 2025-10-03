# %%
import sys
from collections import deque
dxs , dys = [0,0,1,1,1,-1,-1,-1] , [1,-1,1,-1,0,1,-1,0]

sys.stdin = open("input.txt", "r")

N, M = map(int, sys.stdin.readline().split())

space = []
sharks = []
for i in range(N):
    line = list(map(int, sys.stdin.readline().split()))
    for j in range(M):
        if line[j] == 1:
            sharks.append((i,j))
    space.append(line)

distance = [[0 for j in range(M)] for i in range(N)]

Q = deque()
for shark in sharks:
    r, c = shark
    Q.append([r,c])

visited = [[False]*M for _ in range(N)]
while Q:
    r , c = Q.popleft()
    for dx, dy in zip(dxs,dys):
        nr, nc = r + dx, c + dy
        if 0<= nr < N and 0 <= nc < M and not visited[nr][nc] and space[nr][nc] == 0:
            visited[nr][nc] = True
            distance[nr][nc] = distance[r][c] + 1
            Q.append((nr,nc))

ans = -1
for i in range(N):
    for j in range(M):
        ans = max(ans, distance[i][j])
print(ans)
# %%

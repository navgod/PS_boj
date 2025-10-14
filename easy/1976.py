# %%
import sys
from collections import deque
sys.stdin = open("input.txt", "r")

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())


adj = [[] for _ in range(N)]

for i in range(N):
    connected = list(map(int, sys.stdin.readline().split()))
    for j in range(N):
        if connected[j] == 1:
            adj[i].append(j)

plan = list(map(int, sys.stdin.readline().split()))
for i in range(len(plan)):
    plan[i] -= 1

visited = [-1]* N

q = deque()
q.append(plan[0])

for i in range(N):
    if visited[i] == -1:
        q.append(i)
        visited[i] = i

        while len(q) != 0:
            u = q.popleft()

            for v in adj[u]:
                if visited[v] == -1:
                    q.append(v)
                    visited[v] = i

all_visited = True
for i in range(1,len(plan)):
    if visited[plan[i-1]] != visited[plan[i]]:
        all_visited = False
        break

if all_visited:
    print("YES")
else:
    print("NO")
# %%

# %%
import sys
sys.stdin = open("input.txt", "r") 

N, M = map(int, sys.stdin.readline().split())

adj = [[] for _ in range(N+1)]

for _ in range(N-1):
    u, v, d = map(int , sys.stdin.readline().split())
    adj[u].append((v,d))
    adj[v].append((u,d))

def dfs(u):
    global dis, visited
    visited[u] = True
    for v, d in adj[u]:
        if not visited[v]:
            dis[v] = dis[u] + d
            dfs(v)

for _ in range(M):
    u ,v = map(int , sys.stdin.readline().split())
    visited = [False] * (N+1)
    dis = [0] * (N+1)
    dfs(u)
    print(dis[v])
# %%
import sys
from collections import deque
sys.stdin = open("input.txt", "r") 

N, M = map(int, sys.stdin.readline().split())

adj = [[] for _ in range(N+1)]

def bfs(tree, start, end, N):
    visited = [False] * (N+1)
    queue = deque()
    queue.append((start, 0))
    visited[start] = True

    while queue:
        node, dist = queue.popleft()
        if node == end:
            return dist
        for next_node, weight in tree[node]:
            if not visited[next_node]:
                visited[next_node] = True
                queue.append((next_node, dist + weight))

for _ in range(N-1):
    a, b, d = map(int, sys.stdin.readline().split())
    adj[a].append((b, d))
    adj[b].append((a, d))

for _ in range(M):
    u, v = map(int, sys.stdin.readline().split())
    print(bfs(adj, u, v, N))
# %%

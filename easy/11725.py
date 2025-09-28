# %%
import sys
sys.setrecursionlimit(10**6)
sys.stdin = open("input.txt", "r")

N = int(sys.stdin.readline())
adj = [[] for _ in range(N+1)]
for _ in range(N-1):
    u, v = map(int , sys.stdin.readline().split())

    adj[u].append(v)
    adj[v].append(u)

visited = [False] * (N+1)
parent = [-1] * (N+1)

def dfs(u):
    visited[u] = True

    for v in adj[u]:
        if not visited[v]:
            visited[v] = True
            parent[v] = u
            dfs(v)
dfs(1)

for i in range(2,N+1):
    print(parent[i])
# %%

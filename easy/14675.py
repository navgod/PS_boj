# %%
import sys

N = int(sys.stdin.readline())
adj = [[] for _ in range(N+1)]

for _ in range(N-1):
    u, v = map(int ,sys.stdin.readline().split())

    adj[u].append(v)
    adj[v].append(u)
q = int(sys.stdin.readline())
for _ in range(q):
    t, k = map(int ,sys.stdin.readline().split())
    if t == 1:
        if len(adj[k]) == 1:
            print("no")
        else:
            print("yes")
    else:
        print("yes")
# %% 
import sys

sys.stdin = open("input.txt", "r")

N = int(sys.stdin.readline())

parents = list(map(int, sys.stdin.readline().split()))

children = [[] for _ in range(N)]
for i in range(1, N):
    children[parents[i]].append(i)

def dfs(node):
    if not children[node]:
        return 0
    
    child_times = []
    for child in children[node]:
        child_times.append(dfs(child))
    
    child_times.sort(reverse=True)
    
    max_time = 0
    for i, time in enumerate(child_times):
        max_time = max(max_time, (i + 1) + time)
    
    return max_time

print(dfs(0))
# %%

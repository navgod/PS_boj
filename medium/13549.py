# %% 0-1 BFS
import sys
from collections import deque

sys.stdin = open("input.txt", "r")

N, K = map(int, sys.stdin.readline().split())
if N >= K:
    print(N - K)
else:
    MAX = 100001
    dist = [float('inf')] * MAX
    dist[N] = 0

    dq = deque([N])

    while dq:
        x = dq.popleft()
        
        if x == K:
            print(dist[K])
            break
        
        # 순간이동 (0초) - deque 앞에 추가
        nx = x * 2
        if 0 <= nx < MAX and dist[nx] > dist[x]:
            dist[nx] = dist[x]
            dq.appendleft(nx)
        
        # 걷기 (1초) - deque 뒤에 추가
        for nx in [x - 1, x + 1]:
            if 0 <= nx < MAX and dist[nx] > dist[x] + 1:
                dist[nx] = dist[x] + 1
                dq.append(nx)
# %% 다익스트라 
import sys
import heapq

sys.stdin = open("input.txt", "r")

N, K = map(int, sys.stdin.readline().split())

if N>=K:
    print(N-K)
else:
    MAX = 100001
    dist = [float('inf')]* MAX
    dist[N] = 0

    pq = [(0,N)]

    while pq:
        d, x = heapq.heappop(pq)

        if x == K:
            print(d)
            break

        if d > dist[x]:
            continue

        nx = x * 2
        if 0 <= nx < MAX and dist[nx] > d:
            dist[nx] = d
            heapq.heappush(pq, (d, nx))
        
        for nx in [x-1, x+1]:
            if 0 <= nx < MAX and dist[nx] > d + 1:
                dist[nx] = d + 1
                heapq.heappush(pq,(d+1, nx))

# %%

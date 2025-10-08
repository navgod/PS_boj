# %%
import sys
import heapq

sys.stdin = open("input.txt", "r") 

N, K, T = map(int, sys.stdin.readline().split())

A = list(map(int, sys.stdin.readline().split()))
A.sort()

pq = []

pos = 0
for _ in range(K):
    while pos < N and A[pos] < T:
        heapq.heappush(pq,-A[pos])
        pos +=1

    if len(pq) == 0:
        break
    
    T += -heapq.heappop(pq)
print(T)
# %%

# %%
import sys
import heapq

sys.stdin = open("input.txt", "r")

N = int(sys.stdin.readline())
heap = []
for _ in range(N):
    line = list(map(int, sys.stdin.readline().split()))
    for l in line:
        heapq.heappush(heap,l)
        if len(heap)>N:
            heapq.heappop(heap)

print(heap[0])
# %%

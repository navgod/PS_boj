# %%
import sys
from queue import PriorityQueue

sys.stdin = open("input.txt", "r")


N, K = map(int , sys.stdin.readline().split())

A = sys.stdin.readline().rstrip()
pq = PriorityQueue()

for i in range(N):
    if A[i] == 'H':
        pq.put(i)

cnt = 0
for i in range(N):
    if A[i] == 'P':
        while pq.qsize() > 0:
            x = pq.get()

            if abs(x - i) <= K:
                 cnt +=1
                 break
            elif x < i:
                continue
            else:
                pq.put(x)
                break
print(cnt)
# %%

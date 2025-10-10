# %%
import sys
from queue import PriorityQueue
from collections import deque
sys.stdin = open("input.txt", "r") 

N, K = map(int , sys.stdin.readline().split())

info = [list(map(int , sys.stdin.readline().split())) for _ in range(N)]
knapsack = [int(sys.stdin.readline()) for _ in range(K)]
info.sort(reverse= True)
knapsack.sort(reverse= True)

pq = PriorityQueue()
pointer = len(info)-1
ans = 0 
while True:
    if len(knapsack) == 0:
        break
    C = knapsack.pop()
    while pointer >= 0:
        if info[pointer][0] <= C:
            _, V = info.pop()
            pq.put(-V)
            pointer -= 1
        else:
            break
    if pq.qsize() > 0:
        ans += -pq.get()
print(ans)

# %%

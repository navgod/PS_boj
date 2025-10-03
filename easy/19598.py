# %%
import sys
import heapq

sys.stdin = open("input.txt", "r")

N = int(sys.stdin.readline())
meetings = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
meetings.sort()
rooms = []

heapq.heappush(rooms, meetings[0][1])

for room in range(1,N):
    s, e = meetings[room]

    if rooms and rooms[0] <= s:
        heapq.heappop(rooms)
    heapq.heappush(rooms, e)
print(len(rooms))


# %%

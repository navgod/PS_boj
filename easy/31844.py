# %%
import sys

sys.stdin = open("input.txt",  "r")

status = sys.stdin.readline().rstrip()
for i, s  in enumerate(status):
    if s == '@':
        robot_idx = i
    elif s == '#':
        box_idx = i
    elif s == '!':
        goal_idx = i

if (goal_idx - box_idx) * (box_idx - robot_idx) < 0:
    print(-1)
else:
    print(abs(goal_idx-robot_idx)-1)

# %%

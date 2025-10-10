# %%
import sys

sys.stdin = open("input.txt", "r") 

N, M = map(int ,sys.stdin.readline().split())
stacks = []

ordered = True

for i in range(M):
    if not ordered:
        break
    len_stack = int(sys.stdin.readline())
    stack = list(map(int ,sys.stdin.readline().split()))
    for j in range(1,len_stack):
        if stack[j-1] < stack[j]:
            ordered = False
            break
if not ordered:
    print("No")
else:
    print("Yes")
# %%

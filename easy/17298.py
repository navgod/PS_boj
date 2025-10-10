# %%
import sys

sys.stdin = open("input.txt", "r") 

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
stack = []
NGE = [-1] * N
for i in range(len(A)-1,-1,-1):
    now = A[i]
    while len(stack)>0 and stack[-1] <= now:
        stack.pop()
    if len(stack) > 0:
        NGE[i] = stack[-1]
    stack.append(now)
print(*NGE)
# %%

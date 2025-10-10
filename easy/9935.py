# %%
import sys

sys.stdin = open("input.txt", "r") 

string = sys.stdin.readline().strip()
keyword = list(sys.stdin.readline().strip())

k = len(keyword)
stack = []

for s in string:
    stack.append(s)
    if len(stack) >= k and stack[-k:] == keyword:
        for _ in range(k):
            stack.pop()

if len(stack)> 0:
    print(''.join(stack))
else:
    print("FRULA")
# %%

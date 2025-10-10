# %%
import sys

sys.stdin = open("input.txt", "r") 

N = int(sys.stdin.readline().strip())

balls = [[] for _ in range(2001)]
ans = [0] * N
for i in range(N):
    color , size = map(int, sys.stdin.readline().split())
    balls[size].append((i,color))
acuum = 0
color_acuum = {}
for i in range(2001):
    for idx, color in balls[i]:
        if color in color_acuum:
            ans[idx] = acuum - color_acuum[color]
        else:
            ans[idx] = acuum
    for idx, color in balls[i]:
        if color in color_acuum:
            color_acuum[color] += i
        else:
            color_acuum[color] = i
    acuum += len(balls[i])*i

for i in range(N):
    print(ans[i])
# %%

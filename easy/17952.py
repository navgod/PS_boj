# %%
import sys

sys.stdin = open("input.txt", "r")

N = int(sys.stdin.readline())
homework = []
point = 0
for _ in range(N):
    line = sys.stdin.readline().rstrip()
    if line == '0':
        if homework:
            A, T = homework.pop()
            if T <= 1:
                point += A
            else:
                homework.append([A,T-1])
    else:
        _ , A , T = map(int, line.split())
        if T <= 1:
            point += A
        else:
            homework.append([A,T-1])
print(point)
# %%

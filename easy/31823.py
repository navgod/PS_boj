# %%
import sys

sys.stdin = open("input.txt", "r")

N, M = map(int , sys.stdin.readline().split())
reverse_streaks = []
names = []
for _ in range(N):
    A = list(sys.stdin.readline().split())
    name, A = A[-1], A[:-1]
    reverse_streak = 0
    streak = 0
    for item in A:
        if item == '*':
            reverse_streak = max(reverse_streak, streak)
            streak = 0
        else:
            streak += 1
    reverse_streak = max(reverse_streak, streak)
    reverse_streaks.append(reverse_streak)
    names.append(name)
print(len(set(reverse_streaks)))
for i in range(N):
    print(reverse_streaks[i], names[i])


# %%

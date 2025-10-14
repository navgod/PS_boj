# %%
import sys

sys.stdin = open("input.txt", "r")

N = int(sys.stdin.readline())

for _ in range(N):
    words = sys.stdin.readline().rsplit()
    for word in words:
        print(word[::-1], end=" ")
    print()
# %%

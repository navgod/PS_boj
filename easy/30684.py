# %%
import sys

sys.stdin = open("input.txt",  "r")
N = int(sys.stdin.readline())
names = [name for _ in range(N) if len(name := sys.stdin.readline().rstrip()) == 3]
names.sort()

print(names[0])
# %%

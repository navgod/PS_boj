# %%
import sys

sys.stdin = open("input.txt", "r")
N = int(sys.stdin.readline())
box = list(range(N))

while len(box) > 1:
    new_box = []
    for i in range(len(box)):
        if i % 2 != 0:
            new_box.append(box[i])
    box = new_box

print(box[-1]+1)

# %%

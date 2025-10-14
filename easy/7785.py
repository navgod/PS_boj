# %%
import sys

sys.stdin = open("input.txt", "r")

N = int(sys.stdin.readline())

in_people = {}
for _ in range(N):
    name, go = sys.stdin.readline().split()
    if go == "enter":
        in_people[name] = 1
    else:
        del in_people[name]
in_people = sorted([k for k in in_people], reverse=True)
for person in in_people:
    print(person)
# %%

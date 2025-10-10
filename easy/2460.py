# %%
import sys

sys.stdin = open("input.txt", "r") 
people = 0
ans = float('-inf')
for _ in range(10):
    get_out, get_in = map(int, sys.stdin.readline().split())
    people = people - get_out + get_in
    ans = max(ans, people)

print(ans)
# %%

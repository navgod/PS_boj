# %%
import sys
from itertools import permutations

def matching(candidate:str,ask:str,strike:int, ball:int)-> bool:
    matching_num = 0 
    for i in set(candidate):
        if i in set(ask):
            matching_num += 1
    st = 0
    for i in range(3):
        if candidate[i] == ask[i]:
            st += 1
    ba = matching_num - st
    return strike == st and ball == ba


sys.stdin = open("input.txt", "r")

N = int(sys.stdin.readline())

asks = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
ans = 0
for comb in permutations(list(range(1,10)),3):
    candidate = ''.join([str(c) for c in comb])
    is_match = True
    for case in asks:
        ask , strike, ball = case
        ask = str(ask)
        if not matching(candidate,ask, strike, ball):
            is_match = False
            break
    if is_match:
        ans += 1

print(ans)
# %%
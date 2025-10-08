# %%
import sys

sys.stdin = open("input.txt", "r") 

N, Q = map(int , sys.stdin.readline().split())
S = list(sys.stdin.readline().rstrip())

def cnt_sub_alpha(S):
    cnt = 1
    for i in range(1,len(S)):
        if S[i] != S[i-1]:
            cnt +=1

    return cnt

for _ in range(Q):
    query, l, r = map(int, sys.stdin.readline().split())
    if query == 1:
        print(cnt_sub_alpha(S[l-1:r]))
    else:
        for i in range(l-1,r):
            S[i] = chr(ord(S[i])+1) if S[i] != 'Z' else 'A'
# %%

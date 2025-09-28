# %%
import sys
sys.stdin = open("input.txt", "r")
N = int(sys.stdin.readline())

cnt = 0
for _ in range(N):
    word = sys.stdin.readline()
    shorten = ""
    for i in range(len(word)):
        if i == 0 or word[i] != word[i-1]:
            shorten += word[i]
    check = {}
    is_group = True
    for s in shorten:
        if s in check:
            is_group = False
        else:
            check[s] = 1
    if is_group:
        cnt +=1
print(cnt)
# %%

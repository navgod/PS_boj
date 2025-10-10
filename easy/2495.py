# %%
import sys
from collections import defaultdict

sys.stdin = open("input.txt", "r") 

for _ in range(3):
    num = list(sys.stdin.readline().strip())
    cnt, ans = 0, 0
    for i in range(len(num)):
        if i == 0 or num[i-1] == num[i]:
            cnt +=1
        else:
            cnt = 1
        ans= max(ans, cnt)
    print(ans)

# %%
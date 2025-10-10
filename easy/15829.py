# %%
import sys

sys.stdin = open("input.txt", "r") 

r , M = 31, 1234567891

L = int(sys.stdin.readline())
string = sys.stdin.readline().strip()
ans = 0
for i in range(L):
    ans = (ans + (ord(string[i])-ord('a')+1)* r**i )% M
print(ans)
# %%

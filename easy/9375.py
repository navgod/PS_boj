# %%
import sys
import math
from collections import Counter

sys.stdin = open("input.txt", "r")

T = int(sys.stdin.readline())

for _ in range(T):
    N = int(sys.stdin.readline())
    
    if N == 0:
        print(0)
        continue
        
    genres = [sys.stdin.readline().rstrip().split()[1] for _ in range(N)]
    wear_counts = Counter(genres)
    ans = 1
    for count in wear_counts.values():
        ans *= count+1
    print(ans - 1)

# %%
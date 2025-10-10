# %%
import sys

sys.stdin = open("input.txt", "r") 
ans = [
    ['d','d','d'],
    ['d','c','b'],
    ['d','b','a']
]
for _ in range(4):
    x1, y1, p1, q1, x2, y2, p2, q2 = map(int , sys.stdin.readline().split())
    if p1 < x2 or p2 < x1:
        x_intersection = 0
    elif p1 == x2 or x1 == p2:
        x_intersection = 1
    else:
        x_intersection = 2
    if q1 < y2 or q2 < y1:
        y_intersection = 0
    elif q1 == y2 or q2 == y1:
        y_intersection = 1
    else:
        y_intersection = 2

    print(ans[x_intersection][y_intersection])
    

# %%

# %%
import sys

sys.stdin = open("input.txt", "r") 

N = int(sys.stdin.readline())
weight_limit = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
weight = list(map(int, sys.stdin.readline().split()))
weight_limit.sort(reverse= True)
weight.sort(reverse= True)

if weight_limit[0] < weight[0]:
    print(-1)
else:
    cnt = 0
    while len(weight) > 0:
        for crane in weight_limit:
            if len(weight) > 0 and crane < weight[-1]:
                break
            for cargo in weight:
                if crane >= cargo:
                    weight.remove(cargo)
                    break
        cnt +=1
    print(cnt)
# %%

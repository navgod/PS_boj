# %%
import sys

sys.stdin = open("input.txt", "r") 

candidate = [[0] *4 for _ in range(3)]
N = int(sys.stdin.readline())
for _ in range(N):
    x, y, z = map(int, sys.stdin.readline().split())
    candidate[0][x-1] +=1
    candidate[1][y-1] +=1
    candidate[2][z-1] +=1

for i in range(3):
    candidate[i][3] = candidate[i][0] + candidate[i][1] * 2 + candidate[i][2] *3

sorted_cand = sorted(enumerate(candidate), key= lambda x: (x[1][3],x[1][2],x[1][1]), reverse= True)

if sorted_cand[0][1] == sorted_cand[1][1]:
    print(0, sorted_cand[0][1][3])
else:
    print(sorted_cand[0][0]+1, sorted_cand[0][1][3])
# %%

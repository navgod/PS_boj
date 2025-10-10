# %%
import sys

sys.stdin = open("input.txt", "r") 

N, P = map(int ,sys.stdin.readline().split())

num_list = [N]
cycle = set()
num = N
while True:
    num = (num*N)%P
    if num not in cycle:
        num_list.append(num)
        cycle.add(num)
    else:
        break
print(len(num_list[num_list.index(num):]))
# %%

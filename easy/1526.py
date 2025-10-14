# %%
import sys
from itertools import product

sys.stdin = open("input.txt", "r")

nums = []
for i in range(1,7):
    for pro in product([4,7],repeat=i):
        nums.append(int(''.join(map(str,pro))))
nums.sort()
N = int(sys.stdin.readline())
if N > nums[-1]:
    print(nums[-1])
else:
    for i in range(len(nums)):
        if nums[i] > N:
            print(nums[i-1])
            break

# %%

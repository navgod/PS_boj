# %%
import sys
import math

sys.stdin = open("input.txt", "r") 

N = int(sys.stdin.readline())
A = [int(sys.stdin.readline()) for _ in range(N)]
gap = set(A[i]-A[i-1] for i in range(1,N))

gcd = math.gcd(*list(gap))

total = A[-1] - A[0]
print(total//gcd+1-len(A))
# %%

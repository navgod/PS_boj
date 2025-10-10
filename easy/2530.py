# %%
import sys

sys.stdin = open("input.txt", "r") 

A, B, C = map(int, sys.stdin.readline().split())

D = int(sys.stdin.readline())

H, M, S = D//3600, (D%3600)//60 , D%60

C = C + S
if C >= 60:
    C %=60
    M += 1
B += M
if B >= 60:
    B %=60
    H += 1
A += H
if A >= 24:
    A %= 24
print(A, B , C)
# %%

# %%
import math


T = int(input())

for case in range(T):
    M, N, x, y = map(int , input().split())
    # 1~ M 1 ~ N , x = (k-1) % M  + 1 , y = (k-1) % N +1 결국 k는 1부터 M,N의 최소 공배수 까지만 가능 
    max_year = math.lcm(M, N)

    if M < N:
        M, N = N, M
        x, y = y, x
    
    k = x
    solved = False
    while k <= max_year:
        if (k - y) % N == 0:
            print(k)
            solved = True
            break
        k += M
    
    if not solved:
        print(-1)
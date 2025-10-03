# %%
import sys

sys.stdin = open("input.txt", "r")

N = int(sys.stdin.readline())
k = int(sys.stdin.readline())

left, right = 1, k
ans = 0

# 이분 탐색 시작
while left <= right:
    mid = (left + right) // 2
    
    # mid보다 작거나 같은 수의 개수를 계산
    count = 0
    for i in range(1, N + 1):
        count += min(N, mid // i)
        
    # 개수가 k보다 크거나 같으면, mid는 답이 될 수 있음
    # 더 작은 값도 가능한지 계속 탐색
    if count >= k:
        ans = mid
        right = mid - 1
    # 개수가 k보다 작으면, mid는 너무 작은 값이므로 더 큰 값을 탐색
    else:
        left = mid + 1

print(ans)

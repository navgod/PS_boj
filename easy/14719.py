# %%
import sys

sys.stdin = open("input.txt", "r")

H, W = map(int , sys.stdin.readline().split())

heights = list(map(int , sys.stdin.readline().split()))

left, right = 0, W - 1
max_l, max_r = 0, 0
total_rain = 0

while left < right:
    # 더 낮은 쪽을 기준으로 물 높이가 결정됨
    if heights[left] < heights[right]:
        if heights[left] > max_l:
            max_l = heights[left]
        else:
            total_rain += max_l - heights[left]
        left += 1
    else: # heights[left] >= heights[right]
        if heights[right] > max_r:
            max_r = heights[right]
        else:
            total_rain += max_r - heights[right]
        right -= 1
        
print(total_rain)
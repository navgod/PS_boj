# %% 
import sys

sys.stdin = open("input.txt", "r")

N, L, D = map(int, sys.stdin.readline().split())

bell_time = 0

while True:
    song_num = bell_time // (L + 5)
    time_in_cycle = bell_time % (L + 5)
    
    if song_num >= N or time_in_cycle >= L:
        print(bell_time)
        break
    
    bell_time += D
# %%

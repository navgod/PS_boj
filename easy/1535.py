# %%
import sys

sys.stdin = open("input.txt", "r") 

N = int(sys.stdin.readline())

energy = list(map(int, sys.stdin.readline().split()))
happiness = list(map(int, sys.stdin.readline().split()))

max_happy = -1

def back_tracking(idx, now_energy,now_happiness):
    global max_happy, happiness, energy
    if idx == N:
        max_happy = max(max_happy,now_happiness)
        return
    if now_energy > energy[idx]:
        back_tracking(idx+1, now_energy- energy[idx], now_happiness + happiness[idx])
    back_tracking(idx+1,now_energy,now_happiness)

back_tracking(0,100,0)

print(max_happy)
# %%

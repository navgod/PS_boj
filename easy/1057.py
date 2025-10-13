# %%
import sys

sys.stdin = open("input.txt", "r")

N, kim, lim = map(int, sys.stdin.readline().split())

players = list(range(1,N+1))

round = 0
found = False
while not found:
    winners = []
    for i in range(0, len(players)-1,2):
        if players[i] in [kim,lim] and players[i+1] in [kim,lim]:
            found = True
            break
        if players[i] in [kim, lim]:
            winners.append(players[i])
        else:
            winners.append(players[i+1])
    if len(players) % 2 == 1:
        winners.append(players[-1])
    players = winners
    round +=1 

print(round)
# %%

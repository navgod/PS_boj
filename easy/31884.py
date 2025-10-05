# %%
import sys

sys.stdin = open("input.txt",  "r")

Q = int(sys.stdin.readline())

board = {}

for _ in range(Q):
    cmd, i = map(int ,sys.stdin.readline().split())
    if i not in board:
        board[i] = 0
    if cmd == 1:
        top = -1
        for j in range(i,i+4):
            if j in board:
                top = max(top, board[j])
            else:
                board[i] = 0
        for j in range(i,i+4):
            board[j] = top + 1
    elif cmd == 2:
        board[i] += 4
    else:
        print(board[i])
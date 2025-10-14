# %% 
import sys

sys.stdin = open("input.txt", "r")

T = int(sys.stdin.readline())

dir_dict ={
    0: (0,1),
    1: (1,0),
    2: (0,-1),
    3: (-1,0)
}
for _ in range(T):
    dir = 0
    commands = sys.stdin.readline().rstrip()
    x,y= 0,0
    x_min , x_max , y_min , y_max = 0, 0, 0, 0
    for command in commands:
        if command == 'F':
            dx,dy = dir_dict[dir]
            x, y = x+ dx, y + dy
            x_min, x_max = min(x_min,x) , max(x_max, x)
            y_min, y_max = min(y_min,y) , max(y_max, y)
        elif command == 'B':
            dx,dy = dir_dict[dir]
            x, y = x - dx, y - dy
            x_min, x_max = min(x_min,x) , max(x_max, x)
            y_min, y_max = min(y_min,y) , max(y_max, y)
        elif command == 'L':
            dir = (dir-1)%4
        else:
            dir = (dir+1)%4
    print( (y_max - y_min) * (x_max-x_min) )
# %%

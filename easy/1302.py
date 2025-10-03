# %%
import sys
sys.stdin = open("input.txt", "r")

book_dict = {}
N = int(sys.stdin.readline())

for _ in range(N):
    name = sys.stdin.readline().rstrip()
    if name not in book_dict:
        book_dict[name] = 1
    else:
        book_dict[name] +=1

print(sorted(book_dict.items(), key= lambda item: (-item[1], item[0]))[0][0])

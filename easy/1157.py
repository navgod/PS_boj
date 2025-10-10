# %%
import sys

sys.stdin = open("input.txt", "r") 

word = sys.stdin.readline().strip().lower()

word_dict = {}

for char in word:
    if char in word_dict:
        word_dict[char] += 1
    else:
        word_dict[char] = 1


word_ordered_list = sorted(list(word_dict.items()), key= lambda x: x[1], reverse= True)

if len(word_ordered_list) > 1 and word_ordered_list[0][1] == word_ordered_list[1][1]:
    print("?")
else:
    print(word_ordered_list[0][0].upper())
# %%

# %%
import sys
from itertools import combinations

sys.stdin = open("input.txt", "r") 

N, K = map(int, sys.stdin.readline().split())
words = [sys.stdin.readline().strip() for _ in range(N)]

if K < 5:
    print(0)
    exit()
elif K == 26:
    print(N)
    exit()

base_letters = {'a', 'n', 't', 'i', 'c'}
candidate_letters = set()
word_char_sets = []

for word in words:
    middle = word[4:-4]
    
    required = set(middle) - base_letters
    word_char_sets.append(required)
    
    candidate_letters.update(required)

num_to_choose = K - 5
max_readable_words = 0

if len(candidate_letters) <= num_to_choose:
    max_readable_words = N
else:
    for combo in combinations(candidate_letters, num_to_choose):
        learned_set = set(combo)
        
        current_readable_words = 0
        for word_set in word_char_sets:
            if word_set.issubset(learned_set):
                current_readable_words += 1
        
        max_readable_words = max(max_readable_words, current_readable_words)

print(max_readable_words)
# %%

# %%
import sys
sys.stdin = open("input.txt", "r")

N = int(sys.stdin.readline())
string = sys.stdin.readline().rstrip()

if not string:
    print(0)
else:
    left = 0
    ans = 0
    char_dict = {}

    for right in range(len(string)):
        char_dict[string[right]] = char_dict.get(string[right], 0) + 1

        while len(char_dict) > N:
            left_char = string[left]
            char_dict[left_char] -= 1
            if char_dict[left_char] == 0:
                del char_dict[left_char]
            left += 1

        ans = max(ans, right - left + 1)

    print(ans)

# %%
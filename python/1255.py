import re
from collections import defaultdict

n = int(input())

for i in range(n):
    test_case = re.sub(r"[^a-z]", "", input().lower())

    map_chars = defaultdict(lambda: 0)

    for char in test_case:
        map_chars[char] += 1

    all_chars = list(map_chars.items())
    all_chars.sort(key=lambda x: x[1], reverse=True)

    top_1_char = all_chars[0]

    top_chars = [c[0] for c in all_chars if c[1] == top_1_char[1]]
    top_chars.sort()
    print("".join(top_chars))

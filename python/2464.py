cypher = input()
lookup = {}
for i, c in enumerate(cypher):
    lookup[c] = chr(i + 97)

result = []
t = input()
for i in t:
    result.append(lookup.get(i))

print("".join(result))


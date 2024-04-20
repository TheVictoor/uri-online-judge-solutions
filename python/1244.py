entries = int(input())

for i in range(entries):
    entry = input().split(" ")
    entry.sort(key=lambda x: len(x), reverse=True)
    print(" ".join(entry))

n_languages = int(input())

languages = {}
labels = []

for language in range(n_languages):
  l = input()
  grettings = input()
  languages[l] = grettings

childs = int(input())

for c in range(childs):
  child = input()
  language = input()
  labels.append(f"{child}\n{languages.get(language)}\n")

for l in labels:
  print(l)

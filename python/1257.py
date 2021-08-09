n_tests = int(input())

for _ in range(n_tests):
  inputs = int(input())
  count = 0
  for current_input_indice in range(inputs):
    current_set = input()
    for current_char_indice, char in enumerate(current_set):
      count += (ord(char) - 65) + current_input_indice + current_char_indice
  print(count)


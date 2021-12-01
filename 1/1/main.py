import math

number_of_increases = -1
previous_depth = -math.inf

with open('1/input.txt', 'r') as file:
  for line in file:
    stripped_line = line.strip()
    if not stripped_line:
      continue

    current_depth = int(stripped_line)

    if current_depth > previous_depth:
      number_of_increases += 1

    previous_depth = current_depth

print(number_of_increases)

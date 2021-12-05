import math

depth = 0
position = 0

with open('2/input.txt', 'r') as file:
  for line in file:
    command, value = line.strip().split(' ')

    if command == 'forward':
      position += int(value)
    elif command == 'down':
      depth += int(value)
    elif command == 'up':
      depth -= int(value)

print(position * depth)

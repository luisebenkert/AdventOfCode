import math

depth = 0
position = 0
aim = 0

with open('2/input.txt', 'r') as file:
  for line in file:
    command, value = line.strip().split(' ')
    value = int(value)

    if command == 'forward':
      position += value
      depth += aim * value
    elif command == 'down':
      aim += value
    elif command == 'up':
      aim -= value

print(position * depth)

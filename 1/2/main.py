def get_sum(items, index):
  return sum([int(i) for i in items[index:index + 3]])

index = 0
number_of_increases = 0

with open('1/input.txt', 'r') as file:
  items = file.read().splitlines()

  previous_depth = get_sum(items, index)
  
  while index < len(items):  
    current_depth = get_sum(items, index + 1)

    if current_depth > previous_depth:
      number_of_increases += 1

    previous_depth = current_depth
    index += 1

  print(number_of_increases)
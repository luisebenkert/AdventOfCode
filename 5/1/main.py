vents_map = {}
overlaps = 0

with open('5/input.txt', 'r') as file:
  for line in file.readlines():
    positions = line.strip().split(' -> ')
    coordinates = [position.split(',') for position in positions]

    x1 = int(coordinates[0][0])
    y1 = int(coordinates[0][1])
    x2 = int(coordinates[1][0])
    y2 = int(coordinates[1][1])

    if x1 != x2 and y1 != y2:
      continue

    for current_x in range(min(x1, x2), max(x1, x2) + 1):
      for current_y in range(min(y1, y2), max(y1, y2) + 1):
        new_value = vents_map.get(current_y, {}).get(current_x, 0) + 1
        if new_value == 2:
          overlaps += 1
        vents_map.setdefault(current_y, {})[current_x] = new_value

print(overlaps)
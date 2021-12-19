def update_map(vents_map, overlaps, current_x, current_y):
  new_value = vents_map.get(current_y, {}).get(current_x, 0) + 1
  if new_value == 2:
    overlaps += 1
  vents_map.setdefault(current_y, {})[current_x] = new_value
  return overlaps

def main():  
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
        min_x = min(x1, x2)
        max_x = max(x1, x2)
        min_y = y1 if x1 < x2 else y2
        max_y = y1 if x1 > x2 else y2

        current_x = min_x
        current_y = min_y

        while current_x < max_x + 1:
          overlaps = update_map(vents_map, overlaps, current_x, current_y)
          current_x += 1
          current_y += 1 if min_y < max_y else -1
      else:
        for current_x in range(min(x1, x2), max(x1, x2) + 1):
          for current_y in range(min(y1, y2), max(y1, y2) + 1):
            new_value = vents_map.get(current_y, {}).get(current_x, 0) + 1
            if new_value == 2:
              overlaps += 1
            vents_map.setdefault(current_y, {})[current_x] = new_value

  print(overlaps)

main()
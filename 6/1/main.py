with open('6/input.txt', 'r') as file:
  for line in file.readlines():
    all_fish = [int(fish) for fish in line.strip().split(',')]

for x in range(80):
  for index, fish in enumerate(all_fish.copy()):
    if fish == 0:
      all_fish[index] = 6
      all_fish.append(8)
    else:
      all_fish[index] = fish - 1

print(len(all_fish))
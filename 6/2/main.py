with open('6/input.txt', 'r') as file:
  for line in file.readlines():
    all_fish = [int(fish) for fish in line.strip().split(',')]

result = 0

number_of_fish = {i: all_fish.count(i) for i in range(9)}

for day in range(256):
  new_fish = number_of_fish[0]
  number_of_fish[0] = 0
  number_of_fish = {i: number_of_fish[i + 1] for i in range(8)}
  number_of_fish[8] = new_fish
  number_of_fish[6] += new_fish

print(sum(number_of_fish.values()))
import statistics
import math

with open('7/input.txt', 'r') as file:
  for line in file.readlines():
    positions = [int(crab) for crab in line.strip().split(',')]

mean = statistics.mean(positions)

final_position_1 = math.floor(mean)
final_position_2 = math.ceil(mean)

fuel_1 = 0
fuel_2 = 0

for position in positions:
  fuel_1 += sum([i for i in range(abs(position - final_position_1) + 1)])
  fuel_2 += sum([i for i in range(abs(position - final_position_2) + 1)])

print(min(fuel_1, fuel_2))
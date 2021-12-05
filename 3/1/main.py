from collections import defaultdict

gamma_rate = ''
epsilon_rate = ''
frequency = defaultdict(lambda: defaultdict(int))

with open('3/input.txt', 'r') as file:
  for line in file:
    bits = line.strip()

    for index, bit in enumerate(bits):
      frequency[index][int(bit)] += 1

for bit in frequency.values():
  if bit[0] > bit[1]:
    gamma_rate += '0'
    epsilon_rate += '1'
  else:
    gamma_rate += '1'
    epsilon_rate += '0'

print(int(gamma_rate, 2) * int(epsilon_rate, 2))

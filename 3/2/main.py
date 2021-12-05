from collections import defaultdict

def get_frequency(numbers):
  frequency = defaultdict(lambda: defaultdict(int))
  for number in numbers:
    for index, bit in enumerate(number):
      frequency[index][int(bit)] += 1

  return frequency

def calculate_rating(numbers, index, use_most_common_bit):
  if len(numbers) == 1:
    return numbers[0]
  
  frequency = get_frequency(numbers)  
  most_common_bit = 1 if frequency[index][1] >= frequency[index][0] else 0
  new_numbers = [i for i in numbers if int(i[index]) == most_common_bit] if use_most_common_bit else [i for i in numbers if int(i[index]) != most_common_bit]

  index += 1
  return calculate_rating(new_numbers, index, use_most_common_bit)

with open('3/input.txt', 'r') as file:  
  all_numbers = file.read().splitlines()

oxygen_number = calculate_rating(all_numbers, 0, True)
co2_number = calculate_rating(all_numbers, 0, False)

print(int(oxygen_number, 2) * int(co2_number, 2))
def get_board_sum(board, line_length):
  board_sum = 0
  for i in range(line_length):
    board_sum += sum(board[i])

  return board_sum

def play_bingo(bingo_numbers, boards, line_length):
  for index, number in enumerate(bingo_numbers):
    for key, board in boards.items():
      solved_board = False
      for line in board.values():
        if number in line:
          line.remove(number)
          if line == []:
            solved_board = True

      if solved_board:
        if len(boards) == 1:
          return number * get_board_sum(board, line_length)

        boards.pop(key)
        return play_bingo(bingo_numbers[index:], boards, line_length)

with open('4/input.txt', 'r') as file:
  bingo_numbers = [int(i) for i in file.readline().strip().split(',')]
  lines = file.read().splitlines()

boards = {}
board_index = 0
line_index = 0
line_length = None

for line in lines:
  if line == '':
    board_index += 1
    line_index = 0
    continue

  numbers = line.split()
  if not line_length:
    line_length = len(numbers)

  for column_index, number in enumerate(numbers):
    boards.setdefault(board_index, {}).setdefault(line_index, []).append(int(number)) 
    boards.setdefault(board_index, {}).setdefault(column_index + line_length, []).append(int(number)) 

  line_index += 1

result = play_bingo(bingo_numbers, boards, line_length)

print(result)
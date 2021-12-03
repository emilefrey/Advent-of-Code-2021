from filehandler import convertToInt

def part1(data):
  input = convertToInt(data)
  increase = 0
  for index in range(1, len(input)):
    if input[index] > input[index-1]:
      increase += 1
  return increase

def part2(data):
  input = convertToInt(data)
  increase = 0
  for index in range(1, len(input) - 2):
    if sum_sliding(input, index) > sum_sliding(input, index-1):
      increase += 1
  return increase

def sum_sliding(data, start_index):
  return data[start_index] + data[start_index + 1] + data[start_index + 2]

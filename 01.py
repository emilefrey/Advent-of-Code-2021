from filehandler import splitFileByNewLine

targetSum = 2020

def part1(data):
  data_array = [int(i) for i in splitFileByNewLine(data)]
  for value in data_array:
    compliment = targetSum - int(value)
    if compliment in data_array:
      return value * compliment
  return "No 2 numbers add to " + str(targetSum)

def part2(data):
  temp = 0
  data_array = [int(i) for i in splitFileByNewLine(data)]
  for value1 in data_array:
    for value2 in data_array:
      temp = value1 + value2
      value3target = targetSum - temp
      if value3target in data_array:
        print(value1 * value2 * value3target)
        return
  return "No 3 numbers add to " + str(targetSum)

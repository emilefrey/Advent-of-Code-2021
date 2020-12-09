import re
from filehandler import splitFileByNewLine

def part1(data):
  total = 0
  data_array = splitFileByNewLine(data)
  for item in data_array:
    x = re.search("(\d+)-(\d+)\s([a-z]):\s([a-z]+)", item)
    if x:
      count = len(re.findall(x[3], x[4]))
      if count in range(int(x[1]), int(x[2]) + 1):
        total +=1
  return total

def part2(data):
  total = 0
  data_array = splitFileByNewLine(data)
  for item in data_array:
    x = re.search("(\d+)-(\d+)\s([a-z]):\s([a-z]+)", item)
    if x:
      if (x[4][int(x[1]) - 1] == x[3]) != (x[4][int(x[2]) - 1] == x[3]):
        total += 1
  return total
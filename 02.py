from filehandler import splitFileByNewLine



def part1(data):
  input = splitFileByNewLine(data)
  horizontal = 0
  depth = 0
  for command in input:
    command, amount = tuple(command.split(" "))
    amount = int(amount)
    if command == "up":
      depth -= amount
    elif command == "down":
      depth += amount
    elif command == "forward":
      horizontal += amount
  return horizontal * depth

def part2(data):
  input = splitFileByNewLine(data)
  horizontal = 0
  depth = 0
  aim = 0
  for command in input:
    command, amount = tuple(command.split(" "))
    amount = int(amount)
    if command == "up":
      aim -= amount
    elif command == "down":
      aim += amount
    elif command == "forward":
      horizontal += amount
      depth += aim * amount
  return horizontal * depth

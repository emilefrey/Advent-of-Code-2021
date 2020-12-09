from filehandler import splitFileByNewLine

def countTrees(array, right, down):
  count = 0
  col = 0
  i = 0
  while(i < len(array)):
    if array[i][col] == '#':
      count += 1
    col += right
    if col >= len(array[i]):
      col = col - len(array[i])
    i += down
  return count

def part1(data):
  return countTrees(splitFileByNewLine(data), 3, 1)

def part2(data):
  map = splitFileByNewLine(data)
  return countTrees(map, 1, 1) * countTrees(map, 3, 1) * countTrees(map, 5, 1) * countTrees(map, 7, 1) * countTrees(map, 1, 2)
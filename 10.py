from filehandler import splitFileByNewLine, convertToInt

def part1(data):
  array = convertToInt(data)
  array.append(0)
  array.append(max(array) + 3)
  array.sort()
  i = 0
  one = 0
  three = 0
  for value in array[:-1]:
    if array[i + 1] - value == 1:
      one += 1
    if array[i + 1] - value == 3:
      three += 1
    i += 1
  return one * three
  
def part2(data):
  tree = {}
  allValues = convertToInt(data)
  allValues.append(0)
  allValues.append(max(allValues) + 3)
  allValues.sort()


  for value in allValues:
    possibilities = []
    for i in range(1, 4):
      if (value + i) in allValues:
        possibilities.append(value + i)
    tree[value] = possibilities


  def find_all_paths(tree, start, end, path=[]):
      path = path + [start]
      if start == end:
        return [path]
      if start not in tree:
        return []
      paths = []
      for node in tree[start]:
        if node not in path:
          newpaths = find_all_paths(tree, node, end, path)
          for newpath in newpaths:
            paths.append(newpath)
      return paths

  def get_counts(start, tree):
    return sum((get_counts(value, tree) + 1) for value in tree[start])

  # def get_counts(start, tree):
  #   for value in tree[start]:
  #     print(value)
  #     return get_counts(value, tree)
  
  return len(find_all_paths(tree, 0, max(allValues)))
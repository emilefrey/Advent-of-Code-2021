
from filehandler import splitFileByBlankLine

def part1(data):
  count = 0
  for response in splitFileByBlankLine(data):
    uniqueChars = set(response)
    if "\n" in uniqueChars:
      uniqueChars.remove("\n")
    count += len(uniqueChars)
  return(count)
  
def part2(data):
  count = 0
  for response in splitFileByBlankLine(data):
    groups = response.split("\n")
    i = 0
    intersection = groups[0]
    while i < len(groups):
      intersection = list(set(intersection) & set(groups[i]))
      i += 1
    if "\n" in intersection:
      intersection.remove("\n")
    count += len(intersection)
  return count
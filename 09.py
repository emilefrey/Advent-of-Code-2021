from filehandler import splitFileByNewLine, convertToInt
  
def part1(data):
  values = convertToInt(data)
  i = 25
  while i < len(values):
    lookback_range = values[i-25: i]
    if not any((values[i] - lookback) in lookback_range for lookback in lookback_range):
      return values[i]
    i+=1
  return "Not Found"

def part2(data):
  part1value = part1(data)
  values = convertToInt(data)
  i = 0
  while i < len(values):
    j = 1
    temp = [values[i]]
    total = temp[0]
    while total < part1value:
      temp.append(values[i+j])
      total += values[i+j]
      if total == part1value:
        return min(temp) + max(temp)
      j+=1
    i+=1
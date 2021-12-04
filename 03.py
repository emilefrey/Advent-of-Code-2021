from filehandler import splitFileByNewLine

def part1(data):
  input = splitFileByNewLine(data)
  finalString, flippedFinalString = determineFinalString(input, "1")
  return(int(finalString, 2) * int(flippedFinalString, 2))

def part2(data):
  input = splitFileByNewLine(data)
  return filterInput(input, True) * filterInput(input, False)


def filterInput(input, match=True):
  finalString, flippedFinalString = determineFinalString(input, "1")
  filtered = input
  for index in range(len(finalString)):
    # make a copy of 
    # for listIndex, binary in enumerate(filtered):
    filtered = list(filter(lambda x: determineIfMatches(finalString[index], x[index], match), filtered))
    if len(filtered) == 1:
      return(int(filtered[0],2))
    finalString, flippedFinalString = determineFinalString(filtered, "1")
  return int(filtered[0],2)

def determineFinalString(input, defaultIfTie):
  lengthOfBinary = len(input[0])
  totalBinaries = len(input)
  finalString = ""
  for index in range(lengthOfBinary):
    sum = 0
    for binaryNumber in input:
      sum += int(binaryNumber[index])
    if sum > totalBinaries/2:
      finalString += "1"
    elif sum < totalBinaries/2:
      finalString += "0"
    else:
      finalString += "1"
  return finalString, flipBits(finalString)

def flipBits(string):
  flipped = ""
  for bit in string:
    if bit == "0":
      flipped += "1"
    elif bit == "1":
      flipped += "0"
  return flipped

def determineIfMatches(testValue, currentValue, match=True):
  if match:
    return testValue == currentValue
  else:
    return testValue != currentValue
  
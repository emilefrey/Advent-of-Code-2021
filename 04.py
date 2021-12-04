from filehandler import splitFileByNewLine, splitFileByBlankLine

def part1(data):
  input = splitFileByBlankLine(data)
  allCalledNumbers = input[0].split(",")
  for index in range(len(allCalledNumbers)):
    numberOfCalls = index + 1
    currentCalledNumbers = allCalledNumbers[:numberOfCalls]
    for bingoBoard in input[1:]:
      winHorizontal = checkHorizontalRowsForWin(bingoBoard, currentCalledNumbers)
      winVertical = checkVerticalRowsForWin(bingoBoard, currentCalledNumbers)
      if winHorizontal or winVertical:
        return calculateWinningValue(bingoBoard, currentCalledNumbers)


def part2(data):
  input = splitFileByBlankLine(data)
  allCalledNumbers = input[0].split(",")
  for index in range(len(allCalledNumbers)):
    numberOfCalls = index + 1
    currentCalledNumbers = allCalledNumbers[:numberOfCalls]
    losses = 0
    losingCard = None
    bingoBoards = input[1:]
    for bingoBoard in bingoBoards:
      winHorizontal = checkHorizontalRowsForWin(bingoBoard, currentCalledNumbers)
      winVertical = checkVerticalRowsForWin(bingoBoard, currentCalledNumbers)
      if not (winHorizontal or winVertical):
        losses += 1
        losingCard = bingoBoard
    if losses == 1:
      # this is a messsssss
      for index in range(len(allCalledNumbers)):
        numberOfCalls = index + 1
        currentCalledNumbers = allCalledNumbers[:numberOfCalls]
        winHorizontal = checkHorizontalRowsForWin(losingCard, currentCalledNumbers)
        winVertical = checkVerticalRowsForWin(losingCard, currentCalledNumbers)
        if winHorizontal or winVertical:
          return calculateWinningValue(losingCard, currentCalledNumbers)

def checkHorizontalRowsForWin(bingoBoard, calledNumbers):
  for horizontalRow in splitFileByNewLine(bingoBoard):
    horizontalRowSet = set(horizontalRow.split())
    matchedNumbers = set(calledNumbers).intersection(horizontalRowSet)
    if (len(matchedNumbers) == 5):
      return True

def checkVerticalRowsForWin(bingoBoard, calledNumbers):
  for index in range(5):
    verticalRowSet = set([bingoRow.split()[index] for bingoRow in splitFileByNewLine(bingoBoard)])
    matchedNumbers = set(calledNumbers).intersection(verticalRowSet)
    if (len(matchedNumbers) == 5):
      return True

def calculateWinningValue(bingoBoard, currentCalledNumbers):
  sumOfUnmarkedNumbers = findSumOfUnmarkedNumbersOnBoard(bingoBoard, currentCalledNumbers)
  return sumOfUnmarkedNumbers * int(currentCalledNumbers[-1])

def findSumOfUnmarkedNumbersOnBoard(bingoBoard, calledNumbers):
  bingoBoardNumbersSet = set(" ".join(splitFileByNewLine(bingoBoard)).split())
  calledNumbersSet = set(calledNumbers)
  numbersNotCalled = bingoBoardNumbersSet-calledNumbersSet
  return sum([int(x) for x in numbersNotCalled])



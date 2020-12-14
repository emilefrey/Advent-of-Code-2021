from filehandler import splitFileByNewLine

def newSeatStatus(seat, count, threshold):
  if seat == 'L' and count == 0:
    return '#', 1
  elif seat == "#" and count >= threshold:
    return 'L', 1
  else:
    return seat, 0

def oldSeatCount(seat):
  if seat == '#':
    return 1
  else:
    return 0

def countAdjacent(seatRow, seatIndex, allRows):
  countAbove = 0
  countBelow = 0
  countSide = 0
  if seatRow != 0:
    if seatIndex == 0:
      countAbove = oldSeatCount(allRows[seatRow-1][seatIndex]) + oldSeatCount(allRows[seatRow-1][seatIndex + 1])
    elif seatIndex == (len(allRows[seatRow]) - 1):
      countAbove = oldSeatCount(allRows[seatRow-1][seatIndex]) + oldSeatCount(allRows[seatRow-1][seatIndex - 1])
    else:
      countAbove = oldSeatCount(allRows[seatRow-1][seatIndex]) + oldSeatCount(allRows[seatRow-1][seatIndex - 1]) + oldSeatCount(allRows[seatRow-1][seatIndex + 1])
  if seatRow != (len(allRows) - 1):
    if seatIndex == 0:
      countBelow = oldSeatCount(allRows[seatRow+1][seatIndex]) + oldSeatCount(allRows[seatRow+1][seatIndex + 1])
    elif seatIndex == (len(allRows[seatRow]) - 1):
      countBelow = oldSeatCount(allRows[seatRow+1][seatIndex]) + oldSeatCount(allRows[seatRow+1][seatIndex - 1])
    else:
      countBelow = oldSeatCount(allRows[seatRow+1][seatIndex]) + oldSeatCount(allRows[seatRow+1][seatIndex - 1]) + oldSeatCount(allRows[seatRow+1][seatIndex + 1])
  if seatIndex == 0:
    countSide = oldSeatCount(allRows[seatRow][seatIndex + 1])
  elif seatIndex == (len(allRows[seatRow]) - 1):
    countSide = oldSeatCount(allRows[seatRow][seatIndex - 1])
  else:
    countSide = oldSeatCount(allRows[seatRow][seatIndex + 1]) + oldSeatCount(allRows[seatRow][seatIndex - 1])
  return countAbove + countBelow + countSide

def firstSeatCanSee(seatRow, seatIndex, allRows, left, right, up, down):
  found = "."
  i = 1
  while found == ".":
    if (seatRow - up*i + down*i < 0) or ((seatRow - up*i + down*i) > (len(allRows) - 1)) or (seatIndex + right*i - left*i) < 0 or ((seatIndex + right*i - left*i) > (len(allRows[seatRow]) -1)):
      return 0
    found = allRows[seatRow - up*i + down*i][seatIndex + right*i - left*i]
    i += 1
  return oldSeatCount(found)

def countFirstSeatCanSee(seatRow, seatIndex, allRows):
  return (
    firstSeatCanSee(seatRow, seatIndex, allRows, 1, 0, 1, 0) +
    firstSeatCanSee(seatRow, seatIndex, allRows, 0, 0, 1, 0) + 
    firstSeatCanSee(seatRow, seatIndex, allRows, 0, 1, 1, 0) +
    firstSeatCanSee(seatRow, seatIndex, allRows, 0, 1, 0, 0) +
    firstSeatCanSee(seatRow, seatIndex, allRows, 0, 1, 0, 1) +
    firstSeatCanSee(seatRow, seatIndex, allRows, 0, 0, 0, 1) +
    firstSeatCanSee(seatRow, seatIndex, allRows, 1, 0, 0, 1) +
    firstSeatCanSee(seatRow, seatIndex, allRows, 1, 0, 0, 0)
  )
  
  
def part1(data):
  allRows = splitFileByNewLine(data)
  updatedRows = allRows[:]
  tempRows = allRows[:]
  seatsUpdated = 1
  test = 0
  while seatsUpdated > 0:
    seatsUpdated =0
    rowIndex = 0
    tempHolder = tempRows[:]
    for row in updatedRows:
      seatIndex = 0
      tempRow = row[:]
      for seat in tempRow:
        response = newSeatStatus(seat, countAdjacent(rowIndex, seatIndex, updatedRows), 4)
        splitted = list(tempRow)
        splitted[seatIndex] = response[0]
        tempRow = "".join(splitted)
        seatsUpdated += response[1]
        seatIndex += 1
      tempHolder[rowIndex] = tempRow
      rowIndex += 1
    updatedRows = tempHolder
    test += 1
  count = 0
  for row in updatedRows:
    for i in row:
      if i == "#":
        count += 1
  return count

def part2(data):
  allRows = splitFileByNewLine(data)
  updatedRows = allRows[:]
  tempRows = allRows[:]
  seatsUpdated = 1
  while seatsUpdated > 0:
    seatsUpdated =0
    rowIndex = 0
    tempHolder = tempRows[:]
    for row in updatedRows:
      seatIndex = 0
      tempRow = row[:]
      for seat in tempRow:
        response = newSeatStatus(seat, countFirstSeatCanSee(rowIndex, seatIndex, updatedRows), 5)
        splitted = list(tempRow)
        splitted[seatIndex] = response[0]
        tempRow = "".join(splitted)
        seatsUpdated += response[1]
        seatIndex += 1
      tempHolder[rowIndex] = tempRow
      rowIndex += 1
    updatedRows = tempHolder
    print(seatsUpdated)
  count = 0
  for row in updatedRows:
    for i in row:
      if i == "#":
        count += 1
  return count


  return
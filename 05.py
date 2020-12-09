import math
from filehandler import splitFileByNewLine
def seatNumber(seat):
  i = 0
  front = 0
  back = 127
  left = 0
  right = 7
  while i <= 6:
    if seat[i] == "F":
      back = back - math.ceil((back-front)/2)
    elif seat[i] == "B":
      front = front + math.ceil((back-front)/2)
    i += 1
  while i <= 9:
    if seat[i] == "L":
      right = right - math.ceil((right - left)/2)
    elif seat[i] == "R":
      left = left + math.ceil((right - left)/2)
    i += 1
  seat = front * 8 + left
  return seat
  
#part 1
def part1(data):
  highestSeat = 0
  for seat in splitFileByNewLine(data):
    seatNum = seatNumber(seat)
    if seatNum > highestSeat:
      highestSeat = seatNum
  print(highestSeat)
  
#part 2
def part2(data):
  allSeats = []
  for i in range(8, 127 * 8 + 7):
    allSeats.append(i)
  for seat in splitFileByNewLine(data):
    allSeats.remove(seatNumber(seat))
  for seat in allSeats:
    if (seat + 1) not in allSeats and (seat - 1) not in allSeats:
      print(seat)
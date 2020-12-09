from filehandler import splitFileByNewLine,splitFileByBlankLine
import re

def accumulated(instructions):
  accumulator = 0
  visited = set()
  i = 0
  while i not in visited and i < len(instructions):
    visited.add(i)
    x = re.match('([a-z]+)\s(.[\d]+)', instructions[i])
    if x.group(1) == 'nop':
      i += 1
    elif x.group(1) == 'acc':
      accumulator += int(x.group(2))
      i += 1
    elif x.group(1) == 'jmp':
      i += int(x.group(2))
  return accumulator, i not in visited

def part1(data):
  instructions = splitFileByNewLine(data)
  return accumulated(instructions)

def part2(data):
  indices_of_nop = set()
  indices_of_jmp = set()
  instructions = splitFileByNewLine(data)
  i = 0
  while i < len(instructions):
    if 'nop' in instructions[i]:
      indices_of_nop.add(i)
    elif 'jmp' in instructions[i]:
      indices_of_jmp.add(i)
    i += 1
  for index in indices_of_nop:
    instructions = splitFileByNewLine(data)
    instructions[index] = instructions[index].replace('nop', 'jmp')
    if accumulated(instructions)[1] == True:
      return(accumulated(instructions))
  for index in indices_of_jmp:
    instructions = splitFileByNewLine(data)
    instructions[index] = instructions[index].replace('jmp', 'nop')
    if accumulated(instructions)[1] == True:
      return(accumulated(instructions))

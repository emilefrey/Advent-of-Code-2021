import re
from filehandler import splitFileByBlankLine

def validPassportFields(array, requireValidValues):
  count = 0
  for passport in array:
    colons = passport.count(":")
    if ((colons == 8) or ((colons == 7) and not ("cid" in passport))):
      if not requireValidValues:
        count += 1
      elif validPassportValues(passport) and requireValidValues:
        count += 1
  return(count)

def validPassportValues(passport):
  passportFieldValues = re.findall("([a-z]{3}):([#a-z0-9]+)", passport)

  def checkHeight(value):
    if ('cm' in value):
      return int(value.replace("cm", "")) in range(150, 194)
    if ('in' in value):
      return int(value.replace("in", "")) in range (59, 77)
    else:
      return False
  
  def checkRange(value, minimum, maximum):
    return re.search("^[0-9]{4}$", value) and (int(value) in range(minimum, maximum + 1))

  def checkHairColor(value):
    return re.search("#[0-9a-f]{6}", value)
  
  def checkEyeColor(value):
    return value in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
  
  def checkPassportID(value):
    return re.search("^[0-9]{9}$", value)

  for fieldValue in passportFieldValues:
    if (
      (fieldValue[0] == 'byr' and checkRange(fieldValue[1], 1920, 2002))
      or (fieldValue[0] == 'iyr' and checkRange(fieldValue[1], 2010, 2020))
      or (fieldValue[0] == 'eyr' and checkRange(fieldValue[1], 2020, 2030))
      or (fieldValue[0] == 'hgt' and checkHeight(fieldValue[1]))
      or (fieldValue[0] == 'hcl' and checkHairColor(fieldValue[1]))
      or (fieldValue[0] == 'ecl' and checkEyeColor(fieldValue[1]))
      or (fieldValue[0] == 'pid' and checkPassportID(fieldValue[1]))
      or (fieldValue[0] == 'cid')
    ):
      continue
    else:
      return False
  return True

def part1(data):
  return validPassportFields(splitFileByBlankLine(data), False)

def part2(data):
  return validPassportFields(splitFileByBlankLine(data), True)

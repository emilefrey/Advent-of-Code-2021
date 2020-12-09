from filehandler import splitFileByNewLine
import re

def setup(data):
  tree = {}
  allRules = splitFileByNewLine(data)
  for rule in allRules:
    bag_color = re.match('(.+?) bags', rule).group(1)
    bag_contains = re.findall('(\d+) (.+?) bag', rule)
    tree[bag_color] = bag_contains
  return tree

def has_shiny_gold_bag(bag_color, tree):
  if bag_color == "shiny gold":
    return 1
  return any(has_shiny_gold_bag(color, tree) for count, color in tree[bag_color])

def part1(data):
  tree = setup(data)
  return sum(has_shiny_gold_bag(color, tree) for color in tree.keys()) -1

def get_counts(bag_color, tree):
  return sum(int(n)*(get_counts(c, tree) + 1) for n,c in tree[bag_color])

def part2(data):
  tree = setup(data)
  return get_counts('shiny gold', tree)

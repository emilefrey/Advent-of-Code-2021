def splitFileByNewLine(file_contents):
  contents_split = file_contents.splitlines()
  return contents_split

def splitFileByBlankLine(file_contents):
  contents_split = file_contents.split("\n\n")
  return contents_split
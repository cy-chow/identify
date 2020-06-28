from definition import * 

def identify(lines):
  """
  This function evaluates a list of C declaration strings and prints the result.
  """
  for line in lines:
    print(line + ':', end = ' ')
    ans = identifier + ' is a'
    line = replace(line)
    print(ans)

def replace(line):
  for datatype in type_dict:
    line = line.replace(datatype, type_dict[datatype])
  line = line.replace(' ', '')
  return line

def array(substr):
  return 0

def function(substr):
  return 0

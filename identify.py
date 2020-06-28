from definition import * 

def identify(lines):
  """
  This function evaluates a list of C declaration strings and prints the result.
  """
  for line in lines:
    # set up the line for parsing
    print(line + ':', end = ' ')
    line = proofread(line)

    ans = identifier + ' is a'
    index = 0
    try:
      index = line.index(identifier)
      while index != 0:
        index = 0
      print(ans + inv_dict[line[0]])
    except ValueError: 
      print('Invalid identifier ' + 
          '(make sure your declaration includes ' + identifier + ')')
    except KeyError:
      print('Invalid data type used')

def proofread(line):
  for datatype in type_dict:
    line = line.replace(datatype, type_dict[datatype])
  line = line.replace(' ', '')
  return line

def array(substr):
  return 0

def function(substr):
  return 0

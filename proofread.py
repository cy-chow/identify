from definition import type_dict

def proofread(line):
  """
  This function sets up the string input to be processed by the parser
  """
  print(f'{line}:', end = ' ')
  for datatype in type_dict:
    line = line.replace(datatype, type_dict[datatype])
  line = line.replace(' ', '')
  return line

from definition import * 

def identify(lines):
  for line in lines:
    line = line.replace(' ', '')
    for datatype in type_dict:
      line = line.replace(datatype, type_dict[datatype])
    print(line)

DEFAULT_IDENTIFIER = 'x'

type_dict = { 
  'char': 'C',
  'int': 'I',
  'long': 'L',
  'short': 'S',
  'void': 'V'
}

inv_dict = {val: key for key, val in type_dict.items()}

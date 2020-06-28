# change the value of identifier if you want to use a different name
identifier = 'x'

type_dict = { 
  'char': 'C',
  'int': 'I',
  'long': 'L',
  'short': 'S',
  'void': 'V'
}

inv_dict = {val: key for key, val in type_dict.items()}

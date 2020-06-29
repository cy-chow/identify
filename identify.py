from definition import * 

def identify(lines):
  """
  This function evaluates a list of C declaration strings 
  and prints the result.
  """
  for line in lines:
    # set up the line for parsing
    line = proofread(line)

    ans = identifier + ' is '
    try:
      start = line.index(identifier) - 1
      end = start + 2
      while start > 0 or end < len(line):
        # Check end index
        if end >= len(line):
          pass
        # Identify functions
        elif line[end] == '(':
          ans += 'function '
          end += 1
          if line[end] != ')':
            ans += 'taking '
            while line[end] != ')':
              if line[end] == ',':
                ans += 'and '
              elif line[end] == '*':
                ans += 'pointer '
              else:
                ans += inv_dict[line[end]] + ' '
              end += 1

            # Identify the parameters of the function
            while line[end] != ')':
              end += 1
          ans += 'returning '
        # Identify arrays
        elif line[end] == '[':
          end += 1
          ans += 'an array of '
          if line[end] != ']':
            ans += 'size '
            while line[end] != ']':
              ans += line[end]
              end += 1
            ans += ' of '
        
        # Check start index
        if start <= 0:
          pass
        # Identify pointers
        elif line[start] == '*':
          ans += 'pointer to '
        
        # Move start and end indices outward
        start -= 1
        end += 1
      print(ans + inv_dict[line[0]])
    
    except ValueError: 
      print('Invalid identifier ' + 
          '(make sure your declaration includes ' + identifier + ')')
    except KeyError:
      print('Invalid data type used')

def proofread(line):
  print(line + ':', end = ' ')
  for datatype in type_dict:
    line = line.replace(datatype, type_dict[datatype])
  line = line.replace(' ', '')
  return line

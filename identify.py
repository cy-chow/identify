from definition import * 
from proofread import proofread

def identify(lines, identifier = DEFAULT_IDENTIFIER):
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
          ans += 'a function '
          end += 1
          if line[end] != ')':
            ans += 'taking '
            while line[end] != ')':
            # Identify the parameters of the function
              if line[end] == ',':
                ans += 'and '
              elif line[end] == '*':
                ans += 'pointer '
              else:
                ans += inv_dict[line[end]] + ' '
              end += 1
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
          end += 1
        # Check start index
        if start <= 0:
          pass
        # Identify pointers
        elif line[start] == '*':
          ans += 'pointer to '
          start -= 1
        
        # Move start and end indices outward
        """
        if start <= 0 or end >= len(line):
          start -= 1
          end += 1
        """
        if line[start] == '(' and line[end] == ')':
          start -= 1
          end += 1
      print(ans + inv_dict[line[0]])
    
    except ValueError: 
      print('Invalid identifier ' + 
          '(make sure your declaration includes ' + identifier + ')')
    except KeyError:
      print('Invalid data type used')

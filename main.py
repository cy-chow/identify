from identify import identify

def main():
  print('Type in the C declaration (or \'f\' to input a .txt file):', end = ' ')
  response = input()

  if response == 'f':
    print('.txt file name:', end = ' ')  
    filename = input()

    try:
      f = open(filename, 'r')
    except IOError:
      print('The file \'' + filename + '\' could not be found.')
      return 0
    response = f.read()

  identify(response.splitlines())

main()

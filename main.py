import argparse
from identify import identify

def main():

  parser = argparse.ArgumentParser(description='pyDeclare')

  parser.add_argument('-f', '--file', metavar='F', type=str,
                    help='newline-separated file containing declarations to parse')
  parser.add_argument('-i', '--identifier', metavar='I', type=str,
                    help='name of variable identifier in the declarations')
  # parse arguments
  args = parser.parse_args()
  file_decl = args.file 
  identifier = args.identifier if args.identifier else DEFAULT_IDENTIFIER

  # parse the file input if needed
  if file_decl:
    try:
      f = open(file_decl, 'r')
      identify(f.read().splitlines(), identifier)
      f.close() 
    except IOError:
      print(f'The file \'{filename}\' could not be found.')
    return 0

  response = ''
  # no file input, so take user input
  while True:
    print('Input a C declaration to parse (or \'exit\' to exit):', end = ' ')
    response = input()
    if response == 'exit':
        return 0
    identify([response], identifier)


if __name__ == "__main__":
    main()

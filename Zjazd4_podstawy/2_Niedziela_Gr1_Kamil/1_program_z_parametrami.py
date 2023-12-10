import argparse

parser = argparse.ArgumentParser(description='Program czyta plik tekstowy')

parser.add_argument('filename', help='nazwa pliku bez rozszerzenia')
parser.add_argument('-m', '--mode', default='r',
                    help='tryb, domyslnie "r" do odczytu')
parser.add_argument('-ex', '--extention', default='txt',
                    help='rozszerzenie, domyslnie ".txt"')
parser.add_argument('-t', '--test')

args = parser.parse_args()

print(f'Nazwa pliku to: {args.filename}')
print(f'Tryb to: {args.mode}')
print(f'Rozszerzenie to: {args.extention}')
print(f'Testowy argument to: {args.test}')

file = args.filename + '.' + args.extention
print(file)
with open(file, args.mode) as file1:
    content = file1.read()
print(content)

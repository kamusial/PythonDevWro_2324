import argparse

parser = argparse.ArgumentParser()

parser.add_argument('filename')

args = parser.parse_args()

print(f'Nazwa pliku to: {args.filename}')

with open(args.filename, 'r') as file1:
    content = file1.read()

print(content)

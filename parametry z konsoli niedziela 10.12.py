import argparse

parser = argparse.ArgumentParser()
parser.add_argument('filename')
parser.add_argument('-m', '--,mode')
parser.add_argument('-ex', '--extension')

args = parser.parse_args()

print(f'nazwa pliku to:  {args.filename}')

with open(args.filename, 'r') as file1:
    content = file1.read()

print(content)
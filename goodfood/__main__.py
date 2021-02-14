from goodfood.parser import *
import argparse

parser = argparse.ArgumentParser('goodfood', description='Parses a recipe into JSON.')
parser.add_argument('URL', help='recipe URL')
args = parser.parse_args()

result = parse(args.URL)
print(result)

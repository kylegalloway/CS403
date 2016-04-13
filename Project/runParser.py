from parser import Parser

def main(filename):
    p = Parser(filename)
    parse_tree = p.parse()
    print(parse_tree)

import sys
if(len(sys.argv) == 2):
    filename = sys.argv[1]
else:
    filename = "redwall/program.rwall"
main(filename)
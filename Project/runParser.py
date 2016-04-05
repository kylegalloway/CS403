from parser import Parser

def main(filename):
    p = Parser(filename)
    parse_tree = p.parse()
    print(parse_tree)

main("program.txt")
# main("bad_program.txt")
from parser import Parser
from conscell import ConsCell

def main(filename):
    p = Parser(filename)
    parse_tree = p.parse()
    prettyPrint(parse_tree)

def prettyPrint(tree):
        print(tree.value)
        prettyPrint(tree.left)
        prettyPrint(tree.right)

main("program.txt")

from parser import Parser

def main(filename):
    p = Parser(filename)
    parse_tree = p.parse()
    prettyPrint(parse_tree)

def prettyPrint(tree):
    if(tree == None):
        # print("NIL")
        pass
    elif(tree.lvalue == "PARSE"):
        prettyPrint(tree.left)
    elif(tree.lvalue == "FILE"):
        prettyPrint(tree.left)
        prettyPrint(tree.right)
    elif(tree.lvalue == "JOIN"):
        prettyPrint(tree.left)
        prettyPrint(tree.right)
    elif(tree.lvalue == "JOIN"):
        prettyPrint(tree.left)
        prettyPrint(tree.right)
    elif(tree.lvalue == "JOIN"):
        prettyPrint(tree.left)
        prettyPrint(tree.right)
    else:
        print(tree.lvalue)
        prettyPrint(tree.left)
        prettyPrint(tree.right)
    
main("small_program.txt")
# main("program.txt")
# main("bad_program.txt")

from environment import Environment
from lexeme import Lexeme

def main():
    env = Environment()
    env.insert(Lexeme("ID", "x"), Lexeme("INTEGER", 1))
    print(env.lookup(Lexeme("ID", "x")).lvalue)
    env.update(Lexeme("ID", "x"), Lexeme("INTEGER", 2))
    print(env.lookup(Lexeme("ID", "x")).lvalue)

    env.insert(Lexeme("ID", "y"), Lexeme("INTEGER", 11))
    print(env.lookup(Lexeme("ID", "y")).lvalue)
    env.update(Lexeme("ID", "y"), Lexeme("INTEGER", 22))
    print(env.lookup(Lexeme("ID", "y")).lvalue)

    print(env.lookup(Lexeme("ID", "x")).lvalue)

main()
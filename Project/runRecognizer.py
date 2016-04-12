from recognizer import Recognizer

def main(filename):
    r = Recognizer(filename)
    r.parse()

import sys
if(len(sys.argv) == 2):
    filename = sys.argv[1]
else:
    filename = "program.txt"
main(filename)
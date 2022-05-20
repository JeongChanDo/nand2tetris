import sys
from code import Code
from test import Test
from parse import Parse

class HackAssembler:
    def __init__(self,file_name):
        self.code = Code()
        self.parser = Parse(file_name)

if __name__ == "__main__":
    assembler = HackAssembler(sys.argv[1])

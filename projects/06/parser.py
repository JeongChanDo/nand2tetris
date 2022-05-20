from code import Code
import sys

class Parse:
    def __init__(self):
        file_name = sys.argv[1]
        extention = file_name.split(".")[1]
        if extention != "asm":
            raise Exception("extention is not asm")
        self.asm_file = open(file_name, "r")
        print("parser init")
        self.lines = self.asm_file.readlines()
        if self.lines == None:
            raise Exception("file is empty")
        self.lines_iter = iter(self.lines)
        self.line = None
        self.iter_cnt = 0
        self.hack_file = open(file_name.split(".")[0]+".hack", "w")

    def has_more_lines(self):
        self.line = next(self.lines_iter)
        self.iter_cnt = self.iter_cnt + 1
        self.line = self.line.strip()
        print(self.line)
        if self.iter_cnt == len(self.lines):
            print("no more line")
            return False
        else:
            return True
    
    def advance(self):
        more_lines_exist = self.has_more_lines()
        if more_lines_exist == True:
            
            self.advance()
        if self.line == None:
            return None
        elif self.line.startswith("//") == True:
            return None
    
    def instruction_type(self):
        pass
    
    def symbol(self):
        pass
    
    def dest(self):
        pass
    
    def comp(self):
        pass
    
    def jump(self):
        pass
    
    def __del__(self):
        self.asm_file.close()
        self.hack_file.close()


if __name__ == "__main__":
    try:
        parser = Parse()
        coder = Code()
    except Exception as e:
        print(e)
    
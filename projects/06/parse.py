class Parse:
    def __init__(self, file_name):
        print(file_name)
        extention = file_name.split(".")[1]
        if extention != "asm":
            raise Exception("extention is not asm")
        self.asm_file = open(file_name, "r")
        self.lines = self.asm_file.readlines()
        if self.lines == None:
            raise Exception("file is empty")
        self.lines_iter = iter(self.lines)
        self.line = None
        self.iter_cnt = 0
        self.hack_file = open(file_name.split(".")[0]+".hack", "w")
        self.advance()
    
    def has_more_lines(self):
        self.iter_cnt = self.iter_cnt + 1
        if self.iter_cnt == len(self.lines):
            return False
        else:
            return True
    
    def advance(self):
        more_lines_exist = self.has_more_lines()
        line = next(self.lines_iter)
        line = line.strip().replace(" ","")
        cur_instruct_type = self.instruction_type(line)
        print(line, cur_instruct_type)
        if cur_instruct_type == 0 or cur_instruct_type ==2:
            line = self.symbol(cur_instruct_type, line)
        else:
            if "=" in line:
                dest = line.split("=")[0]

        if more_lines_exist == True:
            if (line == "") or (line.startswith("//") == True):
                self.advance()
            else:
                self.hack_file.write(line+"\n")
                self.advance()
        else:
            self.hack_file.write(line)
            print("no more line")

    
    """
    A_INSTRUCTION = 0
    C_INSTRUCTION = 1
    L_INSTRUCTION = 2
    """
    def instruction_type(self, line):
        if line.startswith("@"):
            return 0
        elif line.startswith("("):
            return 2
        else:
            return 1
    
    def symbol(self, cur_instruct_type, line):
        if cur_instruct_type == 0:
            return line.replace("@","")
        else:
            return line.replace("(","").replace(")","")
    
    def dest(self):
        pass
    
    def comp(self):
        pass
    
    def jump(self):
        pass
    
    def __del__(self):
        self.asm_file.close()
        self.hack_file.close()

class Code:
    def __init__(self):
        self.jump_dict = {
            "JGT": "001",
            "JEQ": "010",
            "JGE": "011",
            "JLT": "100",
            "JNE": "101",
            "JLE": "110",
            "JMP": "111"
        }

        self.dest_dict = dict()
        dest_list = ["M", "D", "DM", "A", "AM", "AD", "ADM"]
        for val in dest_list:
            self.dest_dict[val] = list("000")
            if "A" in val:
                self.dest_dict[val][0] = "1"
            if "D" in val:
                self.dest_dict[val][1] = "1"
            if "M" in val:
                self.dest_dict[val][2] = "1"
            self.dest_dict[val] = "".join(self.dest_dict[val])

        # zx nx zy ny f no, out

        self.comp_dict = {
            "0"     : "101010",
            "1"     : "111111",
            "-1"    : "111010",
            "A"     : "110000",
            "M"     : "110000",
            "!D"    : "001101",
            "!A"    : "110001",
            "!M"    : "110001",
            "-D"    : "001111",
            "-A"    : "110011",
            "-M"    : "110011",
            "D+1"   : "011111",
            "A+1"   : "110111",
            "M+1"   : "110111",
            "D-1"   : "001110",
            "A-1"   : "110010",
            "M-1"   : "110010",
            "D+A"   : "000010",
            "D+M"   : "000010",
            "D-A"   : "010011",
            "D-M"   : "010011",
            "A-D"   : "000111",
            "M-D"   : "000111",
            "D&A"   : "000000",
            "D&M"   : "000000",
            "D|A"   : "010101",
            "D|M"   : "010101"
        }

    def get_dest(self, dest_cmd):
        if dest_cmd == None:
            return "000"
        return self.dest_dict[dest_cmd]
    
    def get_jump(self, jump_cmd):
        if jump_cmd == None:
            return "000"
        return self.jump_dict[jump_cmd]
    
    def get_comp(self, comp_cmd):
        print(self.comp_dict)
        return "comp result"
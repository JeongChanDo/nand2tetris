import code



if __name__ == "__main__":
    code = code.Code()
    print(code.get_comp("www"))
    tmp = 0b00001
    print(type(tmp))

    print(code.jump_dict)
    print(code.dest_dict)
    print(code.comp_dict)


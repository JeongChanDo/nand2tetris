@16416
D=A
@dest
M=D
@SCREEN
D=A
@cur_addr
M=D
    (LOOP)
@cur_addr
A=M
M=-1
@cur_addr
M=M+1
D=M
@dest
D=D-M
@LOOP
D;JLT
     (END)
@END
0;JMP
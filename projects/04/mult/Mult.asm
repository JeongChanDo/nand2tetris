@R2
M=0
@R0
D=M
@END
D;JEQ
@R1
D=M
@END
D;JEQ
  (LOOP)
@R1
D=M
@R2
M=M+D
@R0
M=M-1
@R0
D=M
@END
D;JEQ
@LOOP
0;JMP
  (END)
@END
0;JMP
// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Mult.asm

// Multiplies R0 and R1 and stores the result in R2.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)
//
// This program only needs to handle arguments that satisfy
// R0 >= 0, R1 >= 0, and R0*R1 < 32768.

// Put your code here
// R0 = 3,  R1 = 4    1+1+1   1+1+1    1+1+1    1+1+1


// if R0 or R1 == 0 -> end
@R0
D=M
@BIG_STOP
D;JEQ
@R1
@BIG_STOP
D;JEQ
@j
D=1
(BIG_LOOP)
// if (j >R1) goto BIG_END
@j
D=M
@R1
D=D-M
@BIG_STOP
D;JGT
// if r0 == 3,  sum==r2 += 3
@i
D=1
(SMALL_LOOP)
// if (i > R0) goto SMALL_END
@i
D=M
@R0
D=D-M
@SMALL_STOP
D;JGT // if i == (R0 + 1) goto SMALL_STOP
@R2
M=M+1
@i
M=M+1
(SMALL_STOP)
@j
M=M+1
(BIG_STOP)
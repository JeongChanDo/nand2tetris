//210 클럭안에 6 * 7 곱연산을 마무리하지 못해 실패
@0 // init R2 as 0
D=A
@R2
M=D
@R0                  // if R0 or R1 == 0 -> end
D=M
@BIG_STOP
D;JEQ
@R1
D=M
@BIG_STOP 
D;JEQ
@j                    // init j(=R0)     -  j * i = result
M=1
(BIG_LOOP)        //--start of big loop--------------------------------
@j                    // make big loop end condition value
D=M
@R0
D=M-D
@BIG_STOP       // if (R0 - j < 0 )  goto BIG_STOP  r0 = 3, d = 4 => 3-4 < 0
D;JLT
@i
M=1
(SMALL_LOOP)   // -----------start of small loop--------------
@i                   //make small loop end condition value
D=M
@R1
D=M-D
@SMALL_STOP  // if (R1 - i < 0 )  goto SMALL_STOP r1 =5, i = 6    -> 5 - 6 < 0
D;JLT
@R2                 //small loop start
M=M+1
@i
M=M+1
@SMALL_LOOP // goto small loop
0;JMP
(SMALL_STOP)   // -----------end of small loop--------------
@j                   //start big loop
M=M+1
@BIG_LOOP
0;JMP               //goto big loop
(BIG_STOP)        //--end of big loop--------------------------------
@BIG_STOP
0;JMP
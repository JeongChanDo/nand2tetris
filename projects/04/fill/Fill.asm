// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Fill.asm

// Runs an infinite loop that listens to the keyboard input.
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel;
// the screen should remain fully black as long as the key is pressed. 
// When no key is pressed, the program clears the screen, i.e. writes
// "white" in every pixel;
// the screen should remain fully clear as long as no key is pressed.

// Put your code here.

@INIT
0;JMP
     (INIT)
@SCREEN  //start screen addr
D=A
@cur_addr //cur screen addr
M=D
@8192      //total screen register num
D=A
@SCREEN
D=M+D
@end_addr // end screen addr
M=D
     (LOOP)
@KBD
D=M
@BLACK     // when key is pressed, val is greater than 0 
D;JGT
@WHITE
0;JMP
     (WHITE)
@cur_addr
D=M
@SCREEN
D=D-M
@LOOP
D;JEQ        // cur_addr ==screen  dont ram[cur_addr]=1 and  cur_addr -= -1
@cur_addr
A=M
M=0
@cur_addr
M=M-1
@LOOP
0;JMP
     (BLACK)
@cur_addr
D=M
@end_addr
D=D-M
@LOOP
D;JEQ         // cur_addr == end__addr dont ran[cur_addr]=-1 and cur_addr+1
@cur_addr
A=M
M=-1         // ram[cur_addr] = -1
@cur_addr
M=M+1      // cur_addr += 1
@LOOP
0;JMP


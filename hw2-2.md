Q2:Consider following symbols, compute a) the Huffman code, b) draw the code tree, c) the average code length, and d) 
    the entropy of the code. 
{(A, 0.25), (B, 0.25), (C, 0.125), (D, 0.125), (E, 0.125), (F, 0.0625), (G, 0.0625)}

a) the Huffman code 
Si	Pi	        Code
A   0.25          00
B   0.25          01
C   0.125        100
D   0.125        101
E   0.125        110
F   0.0625      1110
G   0.0625      1111

b) draw the code tree 
 {(A, 0.25), (B, 0.25), (C, 0.125), (D, 0.125), (E, 0.125), (F, 0.0625), (G, 0.0625)}
   0 \          / 1         0 \          / 1                     0 \          / 1
          0.5                     0.25                                 0.125
                                                       0 \             / 1
                                                              0.25
                                    0 \                        / 1
                                                  0.5
              0 \                                 / 1
                                  1
c) the average code length 
L = Σ{i=1:N} pili = 0.25*2 + 0.25*2 + 0.125*3 + 0.125*3 + 0.125*3 + 0.0625*4 + 0.0625*4
                  =   0.5 + 0.5 + 0.375 + 0.375 + 0.375 + 0.25 + 0.25
                  =     2.625

d) the entropy of the code. 
H = Σ{i=1:N} pi log2(1/pi) = 0.25*2 + 0.25*2 + 0.125*3 + 0.125*3 + 0.125*3 + 0.0625*4 + 0.0625*4
                           = 0.5 + 0.5 + 0.375 + 0.375 + 0.375 + 0.25 + 0.25
                           = 2.625

function g = SqinSQ(lp,lm)
% Pinta un cuadrado exterior entre -lp y +lp y uno interior entre -lm y +lm
g =[2     2     2     2     2     2     2     2;
     lp     lp     lm     lm    -lm    -lp    -lp    -lm;
     lp    -lp     lm    -lm     lm    -lp     lp    -lm;
    -lp     lp    -lm     lm    -lm    -lp    -lp    -lm;
     lp     lp     lm     lm    -lm     lp    -lp     lm;
     1     1     0     0     0     0     1     1;
     0     0     1     1     1     1     0     0];
 
 


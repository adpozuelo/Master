function main
clear all;
x0=0; TolX=0.01; MaxIter=10;
[x,err,xx]=znewtonM('f','df','ddf',x0,TolX,MaxIter);
fprintf('NewtonM x0=0 -> x=%f\n',x);
[x,err,xx]=znewton('f','df',x0,TolX,MaxIter);
fprintf('Newton x0=0 -> x=%f\n',x);
x0=1.2;
[x,err,xx]=znewtonM('f','df','ddf',x0,TolX,MaxIter);
fprintf('NewtonM x0=1.2 -> x=%f\n',x);
[x,err,xx]=znewton('f','df',x0,TolX,MaxIter);
fprintf('Newton x0=1.2 -> x=%f\n',x);
end

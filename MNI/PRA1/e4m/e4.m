function main
clear all;
x0=0; TolX=0.01; MaxIter=10;
[x,err,xx]=znewton('f','df',x0,TolX,MaxIter);
fprintf('x=%.8f\n',x);
syms a; pt=3;
k=(a/(1-a))*sqrt((2*pt)/(2+a));
fprintf('k(%.8f)=%f\n',x,subs(k,a,x));
end

function [x,fx,xx] = znewton(f,df,x0,TolX,MaxIter)
%newton.m to solve f(x) = 0 by using Newton method.
%input: f = ftn to be given as a string ?f? if defined in an M-file
% df = df(x)/dx (If not given, numerical derivative is used.)
% x0 = the initial guess of the solution
% TolX = the upper limit of |x(k) - x(k-1)|
% MaxIter = the maximum # of iteration
%output: x = the point which the algorithm has reached
% fx = f(x(last)), xx = the history of x
h = 1e-4; h2 = 2*h; TolFun=eps;
if nargin == 4 & isnumeric(df), MaxIter = TolX; TolX = x0; x0 = df; end
xx(1) = x0; fx = feval(f,x0);
for k = 1: MaxIter
if ~isnumeric(df), dfdx = feval(df,xx(k)); %derivative function
else dfdx = (feval(f,xx(k) + h)-feval(f,xx(k) - h))/h2; %numerical drv
end
dx = -fx/dfdx;
xx(k+1) = xx(k)+dx; %Eq.(4.4.2)
fx = feval(f,xx(k + 1));
if abs(fx)<TolFun | abs(dx) < TolX, break; end
end
x = xx(k + 1);
if k == MaxIter, fprintf('The best in %d iterations\n',MaxIter); 
end
end
function H = hermit(x0,y0,dy0,x1,y1,dy1)
A = [x0^3 x0^2 x0 1; x1^3 x1^2 x1 1;
3*x0^2 2*x0 1 0; 3*x1^2 2*x1 1 0];
b = [y0 y1 dy0 dy1]'; %Eq.(3.6-2)
H = (A\b)';
double(A)
double(b)
double(H)
function main
x=0:0.01:10;
for i=1:length(x)
    fp(i)=feval('ftest',x(i));
end
xlabel('x');
ylabel('y');
plot(x,fp);
format long
trapezic('ftest',0,10,10)
trapezic('ftest',0,10,100)
trapezic('ftest',0,10,1000)
simpsonc('ftest',0,10,10)
simpsonc('ftest',0,10,100)
simpsonc('ftest',0,10,1000)
end

function power=ftest(x)
e0=100; R=0.08; L=4; tc=L/R;
I=(e0/R)*(1-exp(-x/tc));
power=(I^2)*R;
end

function INTf = trapezic(f,a,b,N)

% Approximation of the integral by the composite trapezoid rule

% Input
%   - f to integrate. 
%   - a : initial node
%   - b : final node
%   - N : number of subintervals


INTf = 0; 
if (abs(b - a) < eps | N <= 0) 
    return; 
end

% Compute the step
h = (b - a)/N;

% Compute the integral

s1  = 0.0;
for k=1:N-1
  x = a +k*h;
  s1 = s1 + feval(f,x);
end

INTf = h/2*(feval(f,a) + feval(f,b)) + h*s1;
end

function INTf = simpsonc(f,a,b,N)

% Approximation of the integral by the composite Simpson's rule

% Input
%   - f to integrate. 
%   - a : initial node
%   - b : final node
%   - N : number of subintervals

INTf = 0; 
if (abs(b - a)<1e-12 | N <= 0)
    return; 
end

% Number of subintervals must be even

if (mod(N,2) ~= 0) 
    N = N + 1; 
end

% Compute the step

h = (b - a)/N;

% Compute the integral

s1=0.0;
for k=1:N/2
    x = a + h*(2*k-1);
    s1 = s1 + feval(f,x);
end
s2 = 0.0;
for k=1:N/2-1
    x = a + h*2*k;
    s2 = s2 + feval(f,x);
end

INTf = h/3*(feval(f,a) + feval(f,b) + 4*s1 + 2*s2);
end


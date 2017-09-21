function main
a=-5; b=5; n=20;
X=[]; Y=[];
for i=0:1:n-1
    X=[X (a+b)/2+(b-a)/2*(cos(i*pi/(n-1)))];
end
for i=1:1:length(X)
    Y=[Y atan(2*X(i))];
end
 P=lagranp(X,Y);
 xx = -5:.01:5;
 syms x;
 fplot(atan(2*x)); hold on;
 plot(xx,polyval(P,xx),X,Y,'or');
 grid; axis([-5 5 -5 5]);
end

function [l,L] = lagranp(x,y)
%Input : x = [x0 x1 ... xN], y = [y0 y1 ... yN]
%Output: l = Lagrange polynomial coefficients of degree N
% L = Lagrange coefficient polynomial
N = length(x)-1; %the degree of polynomial
l = 0;
for m = 1:N + 1
  P = 1;
  for k = 1:N + 1
    if k ~= m 
      P = conv(P,[1 -x(k)])/(x(m)-x(k)); 
    end
  end
  L(m,:) = P; %Lagrange coefficient polynomial
  l = l + y(m)*P; %Lagrange polynomial (3.1.3)
end
end
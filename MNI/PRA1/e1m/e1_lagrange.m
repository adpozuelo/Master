function main
xmin=-5; xmax=5; n=20; % [x0,x1], n = number of nodes
xlength=abs(xmin)+abs(xmax);
d=xlength/(n-1);
x=-5:d:5;
X=[]; Y=[];
for i=1:1:length(x)
    X=[X x(i)];
    Y=[Y atan(2*x(i))];
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
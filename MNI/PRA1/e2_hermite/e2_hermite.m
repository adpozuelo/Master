clear all
xmin=-5; xmax=5; n=5; % [x0,x1], n = number of nodes
xlength=abs(xmin)+abs(xmax);
d=xlength/(n-1);
x=-5:d:5;
X=[]; Y=[]; dy=[];
syms u;
dfu=diff(atan(2*u));
for i=1:1:length(x)
    X=[X x(i)];
    Y=[Y atan(2*x(i))];
    dy=[dy subs(dfu,u,x(i))];
end
 xi = -5:.01:5;
 syms x;
 fplot(atan(2*x)); hold on;
 H = hermits(X,Y,dy); yi = ppval(mkpp(X,H), xi);
 plot(xi,yi,X,Y,'or');
 grid; axis([-5 5 -5 5]);

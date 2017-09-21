function ko=f(xi)
    syms x; pt=3; k=0.05;
    f=(k*(1-x))-x*sqrt((2*pt)/(2+x));
    fplot(f); grid on;
    ko=subs(f,x,xi);
end
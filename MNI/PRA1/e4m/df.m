function dko=df(xi)
    syms x; pt=3;
    f=(6^(1/2)*x)/(2*(1/(x + 2))^(1/2)*(x + 2)^2) - 6^(1/2)*(1/(x + 2))^(1/2) - 1/20;
    dko=subs(f,x,xi);
end

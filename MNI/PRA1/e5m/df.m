function dko=df(xi)
    syms x;
    dp=5*x^4 - 18*x^3 + (69*x^2)/4 + (9*x)/4 - 27/4;
    dko=subs(dp,x,xi);
end

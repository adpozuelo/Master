function ddko=ddf(xi)
    syms x;
    ddp=20*x^3 - 54*x^2 + (69*x)/2 + 9/4;
    ddko=subs(ddp,x,xi);
end

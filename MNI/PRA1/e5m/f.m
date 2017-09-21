function ko=f(xi)
    syms x;
    p=(x^5)-((9*x^4)/2)+((23*x^3)/4)+((9*x^2)/8)-(27*x/4)+(27/8);
    fplot(p); grid on; axis([0.6 2 -0.2 0.2]);
    ko=subs(p,x,xi);
end
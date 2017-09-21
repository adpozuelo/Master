x = [0 1 1 2 2 3 3 2 2 1 1 0];
y = [0 0 1 1 0 0 3 3 2 2 3 3];
pdepoly(x,y);
g = decsg(gd,sf,ns);
g
[p,e,t] = initmesh(g,'hmax',0.1);
pdemesh(p,e,t);

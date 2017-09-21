function r = LoadVector2D(p,e,gN,lp)
np = size(p,2);
ne = size(e,2);
r = zeros(np,1);
for E = 1:ne
    loc2glb = e(1:2,E);
    x = p(1,loc2glb);
    y = p(2,loc2glb);
    len = sqrt((x(1)-x(2))^2+(y(1)-y(2))^2);
    xc = mean(x); yc = mean(y);
    tmp = gN(xc,yc,lp);
    rE = tmp*[1; 1]*len/2;
    r(loc2glb) = r(loc2glb)+rE;
end

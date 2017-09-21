function [fy] = f(y)
g=6.672E-11; m=5.97E24; gm=g*m;
r_s=y(1)*y(1)+y(2)*y(2);
r_c=r_s*sqrt(r_s);
fy(1)=y(3);
fy(2)=y(4);
fy(3)=-gm*y(1)/r_c;
fy(4)=-gm*y(2)/r_c;
end


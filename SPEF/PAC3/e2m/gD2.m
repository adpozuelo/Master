function g = gD2(x,y)
g=0;
if sqrt(x^2+y^2)<1.01, g=1; end % 1st cylinder at T=1
if sqrt((x-5)^2+y^2)<1.01, g=2; end % 2nd cylinder at T=2
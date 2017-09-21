function z = gN(x,y,lp)
z=0;
if (x < -lp+0.001), z=1;
end;
if (x > lp-0.001), z=-1;
end;


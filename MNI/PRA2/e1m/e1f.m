function main
clear all; clf;
tspan=[0 1]; y0=-1; 
df61=inline('((5*exp(5*t))*(y-t)*(y-t))+1','t','y');
h=[0.01 0.02 0.1 0.2 0.25];
for i=1:5
y=eul(h(i));
if i<5, ye(i)=abs(y(length(y))-analitic(1)); end
N=1./h(i);
[t1,yr] = rk4(df61,tspan,y0,N);
if i<5, yrk(i)=abs(yr(length(yr))-analitic(1)); end
fprintf('h=%.2f, |yE(1)-Y(1)|=%f, |yRK4(1)-Y(1)|=%f\n',h(i),abs(y(length(y))-analitic(1)),abs(yr(length(yr))-analitic(1)));
end
clf;
plot([0.01 0.02 0.1 0.2],ye,'r'); hold on;
plot([0.01 0.02 0.1 0.2],yrk,'b'); hold on;
end

function yr = analitic(ti)
syms t;
y=t-exp(-5*t);
yr=subs(y,t,ti); 
end
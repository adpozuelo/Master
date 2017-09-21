function main
clear all; clf;
t = [0:0.01:1]; yt = t-exp(-5*t);
plot(t,yt,'k'); hold on;
axis([0 1 -1 1]);
tspan=[0 1];
df61=inline('((5*exp(5*t))*(y-t)*(y-t))+1','t','y');
y0=-1;
h=0.2; N=1./h;
[t1,yr] = rk4(df61,tspan,y0,N);
plot(t1,yr,'r:'); hold on;
plot(t1,yr,'r*'); hold on;
h=0.1; N=1./h;
[t1,yr] = rk4(df61,tspan,y0,N);
plot(t1,yr,'b:'); hold on;
plot(t1,yr,'b*'); hold on;
h=0.01; N=1./h;
[t1,yr] = rk4(df61,tspan,y0,N);
plot(t1,yr,'g:'); hold on;
plot(t1,yr,'g*');
end


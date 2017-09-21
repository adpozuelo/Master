function main
clear all; clf;
syms t; ya=[]; ti=[];
h=0.1;
y=t-exp(-5*t);
for i=0:h:1
   ya=[ya subs(y,t,i)]; 
   ti=[ti i];
end
t = [0:h:1]; yt = t-exp(-5*t);
plot(t,yt,'k'); hold on;
axis([0 1 -1 1]);
ye=eul(h);
tspan=[0 1];
df61=inline('((5*exp(5*t))*(y-t)*(y-t))+1','t','y');
y0=-1;
N=1./h;
[t1,yr] = rk4(df61,tspan,y0,N);
plot(t1,yr,'r:'); hold on;
plot(t1,yr,'r*'); hold on;
for i=1:length(ti)
fprintf('ti=%f, y(ti)=%f, yE(ti)=%f, yRK4(ti)=%f, |yE(ti)-y(ti)|=%f, |yRK4(ti)-y(ti)|=%f\n',ti(i),ya(i),ye(i),yr(i),abs(ye(i)-ya(i)),abs(yr(i)-ya(i)));
end
end


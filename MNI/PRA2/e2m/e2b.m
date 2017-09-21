function main
clear all;
t0=0; tf=24*60*60; steps=[40 400]; x=[];
x04=[3071 3500 2000]; colors=['r' 'b' 'g'];
for s=1:length(steps)
h=tf./steps(s); t = [t0:h:tf];
for a=1:length(x04)
x1=zeros(1,steps(s)); x2=zeros(1,steps(s)); x3=zeros(1,steps(s)); x4=zeros(1,steps(s));
y0=[4.223E7 0 0 x04(a)];
x1(1)=y0(1); x2(1)=y0(2); x3(1)=y0(3); x4(1)=y0(4);
y=zeros(1,length(y0));
y(1)=y0(1); y(2)=y0(2); y(3)=y0(3); y(4)=y0(4);
for i=1:steps(s)
y=rk4_step(h,y);
x1(i+1)=y(1); x2(i+1)=y(2); x3(i+1)=y(3); x4(i+1)=y(4);
end
% for i=1:steps
% fprintf('%f %f %f %f %f\n',t(i),x1(i),x2(i),x3(i),x4(i));
% end
%plot(x1,x2,colors(a)); hold on;
%fprintf('t(24), x4(0)=%d, x1(step(%d))=%e\n',x04(a),steps(s),x1(length(x1)));
x=[x x1(length(x1))];
end
end
for i=1:3
fprintf('x4(0)=%d, |x1(step(40))-x1(step(400))|=%f\n',x04(i),abs(x(i)-x(i+3)));
fprintf('x4(0)=%d, |x1(step(40))-x1(step(400))/x1(step(40))|=%f\n',x04(i),abs((x(i)-x(i+3))/x(i)));
end
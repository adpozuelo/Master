function main
clear all; clf;
t0=0; tf=24*60*60; steps=40; h=tf./steps; t = [t0:h:tf];
x04=[3071 3500 2000]; colors=['r' 'b' 'g'];
for a=1:length(x04)
x1=zeros(1,steps); x2=zeros(1,steps); x3=zeros(1,steps); x4=zeros(1,steps);
y0=[4.223E7 0 0 x04(a)];
x1(1)=y0(1); x2(1)=y0(2); x3(1)=y0(3); x4(1)=y0(4);
y=zeros(1,length(y0));
y(1)=y0(1); y(2)=y0(2); y(3)=y0(3); y(4)=y0(4);
for i=1:steps
y=rk4_step(h,y);
x1(i+1)=y(1); x2(i+1)=y(2); x3(i+1)=y(3); x4(i+1)=y(4);
end
% for i=1:steps
% fprintf('%f %f %f %f %f\n',t(i),x1(i),x2(i),x3(i),x4(i));
% end
plot(x1,x2,colors(a)); hold on;
end
end
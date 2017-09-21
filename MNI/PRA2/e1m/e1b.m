function main
clear all; clf;
t = [0:0.01:1]; yt = t-exp(-5*t);
plot(t,yt,'k'); hold on;
axis([0 1 -1 1]);
h=0.2;
eul(h);
h=0.1;
eul(h);
h=0.01;
eul(h);
end

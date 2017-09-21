clear all;
m=200; l=1.4; r=(0.5/2); q=3600; c=4200; h=12; us=16; u0=40; u=60;
S=2*pi*r^2+2*pi*r*l;
alpha=(h*S)/(c*m);
beta=(q+(h*S*us))/(c*m);
ba=beta/alpha;
t=(1/alpha)*log(abs((ba-u0)/(ba-u)));
thr=datevec(t./(60*60*24))

%c temperature 8 hours later
t8=3600*8;
u8=((u0-ba)*exp(-alpha*t8))+ba;





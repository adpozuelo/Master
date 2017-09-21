clear all;
e0=100; R=0.08; L=4; tc=L/R;
syms t; h=[0.1 0.2 0.4];
I=(e0/R)*(1-exp(-t/tc));
dI=diff(I);
ddI=diff(dI);
dddI=diff(ddI);
t0=[]; f0=[]; t2=[]; f2=[]; t10=[]; f10=[]; t0f0=[]; t2f2=[]; t10f10=[];
pe0=[]; pe2=[]; pe10=[];
for i=1:1:3
t0=[t0 subs(dI,t,0)];
f0=[f0 double(subs(I,t,0+h(i))-subs(I,t,0-h(i)))/(2*h(i))];
t0f0=[t0f0 abs(double(t0(i)-f0(i)))];
pe0=[pe0 abs(double(((h(i)^2)/6)*subs(dddI,t,0)))];
t2=[t2 subs(dI,t,2)];
f2=[f2 double(subs(I,t,2+h(i))-subs(I,t,2-h(i)))/(2*h(i))];
t2f2=[t2f2 abs(double(t2(i)-f2(i)))];
pe2=[pe2 abs(double(((h(i)^2)/6)*subs(dddI,t,2)))];
t10=[t10 subs(dI,t,10)];
f10=[f10 double(subs(I,t,10+h(i))-subs(I,t,10-h(i)))/(2*h(i))];
t10f10=[t10f10 abs(double(t10(i)-f10(i)))];
pe10=[pe10 abs(double(((h(i)^2)/6)*subs(dddI,t,10)))];
end
for i=1:1:3
    fprintf('t=0, h=%f, AdI(0)=%f, NdI(0)=%f, e=%e, est_err=%e, e-est_err=%e\n',h(i),t0(i),f0(i),t0f0(i),pe0(i),t0f0(i)-pe0(i))
end
for i=1:1:3
    fprintf('t=2, h=%f, AdI(2)=%f, NdI(2)=%f, e=%e, est_err=%e, e-est_err=%e\n',h(i),t2(i),f2(i),t2f2(i),pe2(i),t2f2(i)-pe2(i))
end
for i=1:1:3
    fprintf('t=10, h=%f, AdI(10)=%f, NdI(10)=%f, e=%e, est_err=%e, e-est_err=%e\n',h(i),t10(i),f10(i),t10f10(i),pe10(i),t10f10(i)-pe10(i))
end
plot(t0f0,'r'); hold on;
plot(t2f2,'b'); hold on;
plot(t10f10,'g');


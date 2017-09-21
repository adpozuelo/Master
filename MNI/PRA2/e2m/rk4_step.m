function [yrk] = rk4_step(h,y0)
n=length(y0);
y=zeros(1,n);k1=zeros(1,n);k2=zeros(1,n);k3=zeros(1,n);k4=zeros(1,n);

fy=f(y0);
for i=1:n
    k1(i)=h*fy(i);
end

for i=1:n
    y(i)=y0(i)+0.5*k1(i);
end
fy=f(y);
for i=1:n
    k2(i)=h*fy(i);
end

for i=1:n
    y(i)=y0(i)+0.5*k2(i);
end
fy=f(y);
for i=1:n
    k3(i)=h*fy(i);
end

for i=1:n
    y(i)=y0(i)+k3(i);
end
fy=f(y);
for i=1:n
    k4(i)=h*fy(i);
end

for i=1:n
    y0(i)=y0(i)+((k1(i)+2*k2(i)+2*k3(i)+k4(i))/6.0);
end

for i=1:length(y0)
    yrk(i)=y0(i);
end

end


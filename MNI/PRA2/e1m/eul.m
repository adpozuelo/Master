function [y] = eul(h)
klast = 1./h;
t=0; y(1) = -1;
for i = 1:klast
t=i*h;
y(i + 1) = y(i) + (f((i-1)*h,y(i))*h); 
plot([i - 1 i]*h,[y(i) y(i+1)],'b', i*h,y(i+1),'ro');
hold on;
end
end

function [yf] = f(t,y)
yf= (5*exp(5*t)*((y-t)*(y-t)))+1;
end


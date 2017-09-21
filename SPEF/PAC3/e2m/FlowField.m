function [bx,by] = FlowField(x,y)
a=1; % cylinder radius
Uinf=2; % free stream velocity
for i=1:1:length(x)
if x(i) < 3.0
    
   r2=x(i)^2+y(i)^2; % radius vector squared
   bx(i)=Uinf*(1-a^2*(x(i)^2-y(i)^2)./r2.^2); % x-component of b
   by(i)=-2*a^2*Uinf*x(i)*y(i)/r2.^2; % y-
else
    r2=(x(i)-5)^2+y(i)^2; % radius vector squared
   bx(i)=Uinf*(1-a^2*((x(i)-5)^2-y(i)^2)./r2.^2); % x-component of b
   by(i)=-2*a^2*Uinf*(x(i)-5)*y(i)/r2.^2; % y-
end
end
% if any(x >= 3.0)
%     r2=(x-5).^2+y.^2; % radius vector squared
%     bx=Uinf*(1-a^2*((x-5).^2-y.^2)./r2.^2); % x-component of b
%     by=-2*a^2*Uinf*(x-5).*y./r2.^2; % y-
%end
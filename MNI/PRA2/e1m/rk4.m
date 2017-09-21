function [t,y] = rk4(f,tspan,y0,N,varargin)
%Runge-Kutta method to solve vector differential eqn y?(t) = f(t,y(t))
% for tspan = [t0,tf] and with the initial value y0 and N time steps
if nargin < 4 | N <= 0, N = 100; end
if nargin < 3, y0 = 0; end
y(1,:) = y0(:)'; %make it a row vector
h = (tspan(2) - tspan(1))/N; t = tspan(1)+[0:N]'*h;
for k = 1:N
f1 = h*feval(f,t(k),y(k,:),varargin{:}); f1 = f1(:)'; %(6.3.2a)
f2 = h*feval(f,t(k) + h/2,y(k,:) + f1/2,varargin{:}); f2 = f2(:)';%(6.3.2b)
f3 = h*feval(f,t(k) + h/2,y(k,:) + f2/2,varargin{:}); f3 = f3(:)';%(6.3.2c)
f4 = h*feval(f,t(k) + h,y(k,:) + f3,varargin{:}); f4 = f4(:)'; %(6.3.2d)
y(k + 1,:) = y(k,:) + (f1 + 2*(f2 + f3) + f4)/6; %Eq.(6.3.1)
end
end
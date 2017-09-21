function H = hermits(x,y,dy)
% finds Hermite interpolating polynomials for multiple subintervals
%Input : [x,y],dy - points and derivatives at the points
%Output: H = coefficients of cubic Hermite interpolating polynomials
for n = 1:length(x)-1
H(n,:) = hermit(0,y(n),dy(n),x(n + 1)-x(n),y(n + 1),dy(n + 1));
end
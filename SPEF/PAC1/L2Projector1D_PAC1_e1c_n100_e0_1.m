function L2Projector1D()
n = 100; % number of subintervals
h = 2/n; % mesh size
x = -1:h:1; %mesh
M = MassAssembler1D(x); % assemble mass
b = LoadAssembler1D(x, @adpozuelo); % assemble load
Pf = M\b; % solve linear system
fplot(@adpozuelo,[-1,1]); 
hold on;
plot(x,Pf) % plot L^2 projection
l2_error_quadratic(n,x,Pf,@adpozuelo)
end

function M = MassAssembler1D(x)
n = length(x)-1; % number of subintervals
M = zeros(n+1, n+1); % allocate mass matrix
for i = 1:n % loop over subintervals
    h = x(i+1) - x(i); % interval length
    M(i,i) = M(i,i) + h/3; % add h/3 to M(i,i)
    M(i,i+1) = M(i,i+1) + h/6; 
    M(i+1,i) = M(i+1,i) + h/6;
    M(i+1,i+1) = M(i+1,i+1) + h/3;
end
end

function b = LoadAssembler1D(x,f)
n = length(x)-1;
b = zeros(n+1,1);
for i = 1:n
    h = x(i+1) - x(i);
    b(i) = b(i) + f(x(i)) * h/2;
    b(i+1) = b(i+1) + f(x(i+1)) * h/2;
end
end

function f = adpozuelo(x)
e = 0.1;
f = atan((x-0.5)/e);
end

function e2 = l2_error_quadratic(n,x,u,exact)
e2 = 0.0;
quad_num = 3;
abscissa(1) = -0.774596669241483377035853079956;
abscissa(2) = 0.000000000000000000000000000000;
abscissa(3) = 0.774596669241483377035853079956;
weight(1) = 0.555555555555555555555555555556;
weight(2) = 0.888888888888888888888888888889;
weight(3) = 0.555555555555555555555555555556;
e_num = ( n - 1 ) / 2;
for e = 1 : e_num
    l = 2 * e - 1;
    m = 2 * e;
    r = 2 * e + 1;
    xl = x(l);
    xm = x(m);
    xr = x(r);
    for q = 1 : quad_num
      xq = ( ( 1.0 - abscissa(q) ) * xl + ( 1.0 + abscissa(q) ) * xr ) / 2.0;
      wq = weight(q) * ( xr - xl ) / 2.0;
      vl = ( ( xq - xm ) / ( xl - xm ) ) * ( ( xq - xr ) / ( xl - xr ) );
      vm = ( ( xq - xl ) / ( xm - xl ) ) * ( ( xq - xr ) / ( xm - xr ) );
      vr = ( ( xq - xl ) / ( xr - xl ) ) * ( ( xq - xm ) / ( xr - xm ) );
      uq = u(l) * vl + u(m) * vm + u(r) * vr;
      eq = exact ( xq );
      e2 = e2 + wq * ( uq - eq )^2;
    end
 end
  e2 = sqrt ( e2 );
  return
end


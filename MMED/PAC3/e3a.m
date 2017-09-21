function c_ht_sponcomp
global lambda theta_a;

lambda=2.2;
theta_a=0.27;

syms x;
fplot(exp(-1/x)); hold on;
fplot((lambda)*(x-theta_a));

%fplot(2.2*exp(-1/x)-(x-0.19));hold on; fplot(0);
axis([0.001 1.5 -0.1 0.2]);
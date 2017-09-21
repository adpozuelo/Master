function c_pe_epidemic
global beta gamma N;

tend=20; %end time to run the simulation
u0=[150;40]; %initial conditions as a column vector
beta=0.002; gamma=0.4;
[tsol,usol]=ode45(@rhs,[0,tend],u0);
Ssol=usol(:,1); Isol=usol(:,2);
plot(tsol,Ssol,'r'); hold on; plot(tsol,Isol,'b');
grid on;
max(usol(:,2))

function udash=rhs(t,u)
global beta gamma N;
S=u(1); I=u(2);
lambda=beta*I;
Sdash=-lambda*S;
Idash=lambda*S-gamma*I;
udash=[Sdash;Idash];

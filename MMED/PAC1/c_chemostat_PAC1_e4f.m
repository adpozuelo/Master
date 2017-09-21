function c_chemostat
global v f gamma m a Sin;

tend=20; %end time to run the simulation
u0=[0.5;2]; %initial conditions as a column vector
v=10; f=5; gamma=5; m=5; a=5; Sin=0.1;
[tsol,usol]=ode45(@rhs,[0,tend],u0);
Ssol=usol(:,1); Xsol=usol(:,2);
plot(tsol,Ssol,'r'); hold on; plot(tsol,Xsol,'b');
grid on;
max(Xsol)

function udash=rhs(t,u)
global v f gamma m a Sin;
S=u(1); X=u(2);
ps=(m*S)/(a+S);
Sdash=Sin-((f/v)*S)-(ps*X);
Xdash=gamma*X*ps;
udash=[Sdash;Xdash];

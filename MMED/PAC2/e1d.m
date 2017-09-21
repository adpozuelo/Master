function c_cp_predprey

tend=20; %end time to run the simulation
u0=[0.0000001;0.0000001]; %initial condition as a vector
[tsol,usol]=ode45(@rhs,[0,tend],u0);
Xsol=usol(:,1); Ysol=usol(:,2);
plot(tsol,Xsol,'b'); hold on; plot(tsol,Ysol,'r');
axis([-2 2 -2 2]);

function udot=rhs(t,u)
X=u(1); Y=u(2);
Xdot=X-Y;
Ydot=1-(X*Y);
udot=[Xdot;Ydot];

function HeatFlowSolver2D()
channel=Rect2Circ(); % channel geometry
pdegplot(channel); hold on;
epsilon=0.01; % diffusion parameter
h=0.1; % mesh size
[p,e,t]=initmesh(channel,'hmax',h); % create mesh
A=assema(p,t,1,0,0); % stiffness matrix
x=p(1,:); y=p(2,:); % node coordinates
[bx,by]=FlowField(x,y); % evaluate vector field b
C=ConvectionAssembler2D(p,t,bx,by); % convection matrix
Sd=SDAssembler2D(p,t,bx,by); % GLS stabilization matrix
[R,r]=RobinAssembler2D(p,e,@Kappa2,@gD2,@gN2); % Robin BC
delta=h; % stabilization parameter
U=(epsilon*A-C'+R+delta*Sd)\r; % solve linear system
%pdecont(p,t,U), axis equal % plot solution
pdeplot(p,[],t,'XYData',U,'XYStyle','flat','Contour',...
'on','Levels',20,'ColorBar','on'), axis equal
%pdeplot(p,e,t,'XYdata',U),axis equal
%pdeplot(p,e,t,'flowdata',[bx' by']), axis equal
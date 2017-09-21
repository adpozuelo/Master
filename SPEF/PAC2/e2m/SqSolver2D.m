function SqSolver2D()
g=SqinSQ(1.5,0.5);
pdegplot(g); hold on;
[p,e,t] = initmesh(g,'hmax',0.1);
A=StiffnessAssembler2D(p,t);
r = LoadVector2D(p,e,@gN,1.5);
r;
phi=A\r;
pdecont(p,t,phi,50); hold on;
[phix,phiy]=pdegrad(p,t,phi);
u=-phix';
v=-phiy';
pdeplot(p,e,t,'flowdata',[u,v])


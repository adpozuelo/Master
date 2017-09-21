function A = StiffnessAssembler2D(p,t)
np = size(p,2);
nt = size(t,2);
A = sparse(np,np);
for K=1:nt
    loc2glb = t(1:3,K);
    x=p(1,loc2glb);
    y=p(2,loc2glb);
    [area,b,c] = HatGradients(x,y);
    AK = (b*b'+c*c')*area;
    A(loc2glb,loc2glb) = A(loc2glb,loc2glb)+AK;
end

    